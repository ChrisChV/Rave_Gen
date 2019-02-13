import io
import Utils.sad as sad
import Utils.inputManager as inputManager
import Utils.commandManager as commandManager
import Utils.logManager as logManager
import Utils.utils as utils
import RaveEngine.configManager as configManager


def initConfiguration():
    logManager.printVerbose("Verifying configuration...")
    logManager.printVerbose("Verifying Heroku login...")
    while True:
        if _verifyHerokuLogIn() == False:
            logManager.printVerbose("Can't find heroku token")
            logManager.printVerbose("Heorku login...")
            _herokuLogIn()
        else:
            break
    config = configManager.getConfig()
    projectNameFlag = True
    initProjectFlag = True
    gitInitFlag = True
    gitHerokuFlag = True
    projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
    logManager.printVerbose("Verifiying project name...")
    if projectName != None and projectName != sad._INIT_CONFIG_PROJECT_NAME:
        logManager.printVerbose("Project name found: " + projectName)
        projectNameFlag = False
    logManager.printVerbose("Verifiying project in heroku...")
    if _verifyProject(projectName) == True:
        logManager.printVerbose("The project has already been created in heroku")
        initProjectFlag = False
    if utils.file_Or_Directory_Exists(sad._ACTUAL_PATH, sad._GIT_DIR_) == True:
        logManager.printVerbose("Git has already been created")
        gitInitFlag = False
    if _verifyRemoteHeroku() == True:
        logManager.printVerbose("Git has already been configured")
        gitHerokuFlag = False
    
    _initConfiguration(projectNameFlag, initProjectFlag, gitInitFlag, gitHerokuFlag)
    logManager.printVerbose("All Configurations... OK")

def deploy():
    _crateSkeleton()
    commandManager.runGitAddAll()
    logManager.printVerbose("Commiting changes...")
    commandManager.runGitCommitCommand(utils.getTime() + ": Deploy bot in heroku")
    logManager.printVerbose("Deploying bot in Heroku...")
    commandManager.runGitPushCommand(sad._DEPLOY_HEROKU_OPTION, sad._GIT_MASTER)
    _deleteSkeleton()
    logManager.printVerbose("Deploying bot in Heroku...OK")


def deleteCloudApp():
    config = configManager.getConfig()
    projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
    if projectName != None and projectName != sad._INIT_CONFIG_PROJECT_NAME:
        commandManager.runHerokuDestroyCommand(projectName)
        configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, "")
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, "")
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, "")
        configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_GIT_OPTION_, "")

def _initConfiguration(projectNameFlag = True, initProjectFlag = True, gitInitFlag = True, gitHerokuFlag = True):
    config = configManager.getConfig()
    if projectNameFlag == True:
        logManager.printVerbose("Project name doesn't found")
        _getNewHerokuName(config)
        initProjectFlag = True
    if initProjectFlag == True:
        logManager.printVerbose("Project hasn't been craeted in heroku")
        erroFlag = False
        while True:
            if erroFlag == True:
                logManager.printVerbose("The project can't created in heroku. Read the erros above and chose a new heroku project name")
                _getNewHerokuName(config)
            projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
            token = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
            deployUrl = sad._HTTPS_ + projectName + sad._HEROKU_URL
            gitUrl = sad._HTTPS_ + sad._HEORKU_GIT_URL + projectName + sad._GIT_EXTENTION
            commandManager.runHerokuCreateCommand(projectName)
            if _verifyProject(projectName) == True:
                configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, deployUrl)
                configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, token)
                configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_GIT_OPTION_, gitUrl)
                break
            else:
                erroFlag = True
    if gitInitFlag == True:
        logManager.printVerbose("Creating git...")
        commandManager.runGitInitCommand()
        gitHerokuFlag = True
    if gitHerokuFlag == True:
        logManager.printVerbose("Configuring git...")
        gitUrl = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_GIT_OPTION_)
        commandManager.runGitAddRemoteCommand(sad._DEPLOY_HEROKU_OPTION, gitUrl)


def _crateSkeleton():
    procFile = open(sad._HEROKU_PROCFILE_NAME, 'w')
    procFile.write("web: " + sad._LINUX_PYTHON_COMMAND_ + sad.OUTPUT_BOT_PATH)
    procFile.close()    
    commandManager.runCpCommand(sad._CONFIG_REQ_FILE_PAHT_, sad._HEROKU_REQ_FILE_NAME)    
    commandManager.runCpCommand(sad._CONFIG_RUNTIME_FILE_PATH_, sad._HEROKU_RUNTIME_FILE_NAME)

def _deleteSkeleton():
    commandManager.runRmCommand(sad._HEROKU_PROCFILE_NAME, sad._HEROKU_REQ_FILE_NAME, sad._HEROKU_RUNTIME_FILE_NAME)

def _verifyProject(projectName):
    if projectName == None:
        projectName = "None"
    commandManager.runHerokuInfoCommand(projectName, sad._TEMP_HEROKU_INFO_FILE_NAME)
    tempFile = open(sad._TEMP_HEROKU_INFO_FILE_NAME, 'r')
    count = 0
    line = tempFile.readline()
    tokens = line.split(' ')
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_HEROKU_INFO_FILE_NAME)
    if(tokens[0] == '==='):
        return True
    return False

def _verifyRemoteHeroku():
    commandManager.runGitRemoteCommand(sad._TEMP_GIT_REMOTE_FILE_NAME)
    files = []
    tempFile = open(sad._TEMP_GIT_REMOTE_FILE_NAME, 'r')
    for line in tempFile:
        files.append(line.rstrip('\n'))
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_GIT_REMOTE_FILE_NAME)
    if sad._DEPLOY_HEROKU_OPTION in files:
        return True
    return False

def _verifyHerokuLogIn():
    commandManager.runHerokuToken(sad._TEMP_HEROKU_TOKEN_FILE_NAME)
    tempFile = open(sad._TEMP_HEROKU_TOKEN_FILE_NAME)
    count = 0
    for line in tempFile:
        count += 1
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_HEROKU_TOKEN_FILE_NAME)
    if count > 1:
        return True
    return False

def _herokuLogIn():
    commandManager.runHerokuLogin()

def _getNewHerokuName(config):    
    projectName = inputManager.getInput("Enter new Heroku Project Name: ")
    configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, projectName)
        