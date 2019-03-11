
_DF_ = "/"
_DD_ = ":"

_ACTUAL_PATH = "./"
_RAVEGEN_SRC_PATH_ = "ravegen"
_RAVEGEN_DEV_NAME_ = "ravegen-dev"
_HTTPS_ = "https://"

_HOME_RAVE_PATH_ = "~/.ravegen"
_HOME_RAVE_INSTALLATION_PATH_FILE_NAME = "installationPath"
_HOME_RAVE_INSTALLATION_PATH_FILE = _HOME_RAVE_PATH_ + _DF_ + _HOME_RAVE_INSTALLATION_PATH_FILE_NAME



_PYC_EXTENTION = ".pyc"
_GIT_EXTENTION = ".git"

_GIT_DIR_ = ".git"
_GIT_MASTER = "master"

_STR_TRUE_ = "True"


#_INSTALL_PATH = "/usr/local/lib/python2.7/dist-packages/ravegen/"


_OUTPUT_BOT_NAME_ = "bot.py"
_OUTPUT_BOT_DIR_ = "bot"
_MODULES_DIR_ = "modules"
_MODULES_EXTENTION_ = "py"
_LOG_DIR_NAME_ = "log"
_LOG_FILE_NAME_ = "log"
_LOG_FILE_PATH_ = _LOG_DIR_NAME_ + _DF_ + _LOG_FILE_NAME_
_VERSION_FILE_NAME = "version"
_CONFIG_FILE_NAME_ = "ravegen.conf"
_CONFIG_DIR_NAME_ = "config"
_CONFIG_REQ_FILE_NAME_ = "requirements"
_CONFIG_REQ_FILE_PAHT_ = _CONFIG_DIR_NAME_ + _DF_ + _CONFIG_REQ_FILE_NAME_
_CONFIG_RUNTIME_FILE_NAME_ = "runtime"
_CONFIG_RUNTIME_FILE_PATH_ = _CONFIG_DIR_NAME_ + _DF_ + _CONFIG_RUNTIME_FILE_NAME_
_CONFIG_FILE_PATH = _CONFIG_DIR_NAME_ + _DF_ + _CONFIG_FILE_NAME_
OUTPUT_BOT_PATH = _OUTPUT_BOT_DIR_ +  _DF_ + _OUTPUT_BOT_NAME_



#CONSOLE ENGINE CONSTANTS
_CONSOLE_ENGINE_INFO_OPTION_ = "Info"
_CONSOLE_ENGINE_OPTION_TAG_ = "Options"
_CONSOLE_ENGINE_AUTOCOMPLETITION_FILE_NAME = "rave_compl.bash"
_CONSOLE_ENGINE_COMMANDS_FILE_NAME = "commands"
_CONSOLE_ENGINE_COMMANDS_FILE_DEV_PATH = _RAVEGEN_SRC_PATH_ + _DF_ + "commands" 

_TEMP_LS_MODULES_FILE_NAME = ".tempModuels"
_TEMP_LS_VERIFY_FILE_NAME = ".tempVerifyFiles"
_TEMP_HEROKU_INFO_FILE_NAME = ".tempHerokuInfo"
_TEMP_GIT_REMOTE_FILE_NAME = ".tempGitRemoteInfo"
_TEMP_HEROKU_TOKEN_FILE_NAME = ".tempHerokuToken"
_TEMP_SNAP_LIST_FILE_NAME = ".tempSnapList"
_TEMP_PYTHON_PATH_FILE_NAME = ".tempPythonPath"


_CONFIG_RAVEGEN_SECTION_ = "RaveGen"
_CONFIG_HOSTING_OPTION_ = "hosting"
_CONFIG_TOKEN_OPTION_ = "token"
_CONFIG_DEPLOY_URL_OPTION = "deploy_url"
_CONFIG_DEPLOY_PORT_OPRION = "deploy_port"
_CONFIG_WEBHOOK_PATH_OPTION = "webhook_path"
_CONFIG_PROJECT_NAME_OPTION_ = "project_name"
_CONFIG_GIT_OPTION_ = "git"
_CONFIG_VERBOSE_OPTION_ = "verbose"
_CONFIG_LOG_OPTION_ = "log"

_INIT_CONFIG_TOKEN_ = "__TOKEN__"
_INIT_CONFIG_DEPLOY_URL = "__URL__"
_INIT_CONFIG_DEPLOY_PORT = "__PORT__"
_INIT_CONFIG_WEBHOOK_PATH = "__PATH__"
_INIT_CONFIG_VERBOSE = "yes"
_INIT_CONFIG_LOG = "yes"
_INIT_CONFIG_PROJECT_NAME = "__PROJECT__NAME__"

_HEADER_TOKEN_FLAG = "TokenFlag"


_DEPLOY_HEROKU_OPTION = "heroku"

_HEORKU_SNAP_PACKAGE = "snapd"
_HEROKU_HEROKU_CLI_VERSION_ = "--classic"
_HEROKU_SNAP_PATH = "/usr/bin/snap"
_HEROKU_URL = ".herokuapp.com/"
_HEORKU_GIT_URL = "git.heroku.com/"
_HEROKU_PROCFILE_NAME = "Procfile"
_HEROKU_REQ_FILE_NAME = "requirements.txt"
_HEROKU_RUNTIME_FILE_NAME = "runtime.txt"

_LINUX_SUDO_COMMAND_ = "sudo "
_LINUX_PACKAGE_MANAGER_INSTALL_OPTION = "install "
_LINUX_MKDIR_COMMAND_ = "mkdir -p "
_LINUX_LS_COMMAND_ = "ls -a "
_LINUX_RM_COMMAND_ = "rm -f "
_LINUX_RM_COMMAND_DIR = "rm -Rf "
_LINUX_CP_COMMAND_ = "cp "
_LINUX_CP_DIR_COMMAND_ = "cp -R "
_LINUX_ECHO_COMMAND_ = "echo "
_LINUX_GIT_COMAND_ = "git "
_LINUX_GIT_INIT_COMMAND_ = "init "
_LINUX_GIT_ADD_OPTION_ = "add "
_LINUX_GIT_ALL_OPTION_ = "--all "
_LINUX_GIT_REMOTE_OPTION_ = "remote "
_LINUX_GIT_REMOTE_SET_URL_OPTION = "set-url "
_LINUX_GIT_REMOTE_VERBOSE_OPTION = "-v "
_LINUX_GIT_COMMIT_OPTION_ = "commit -m '"
_LINUX_GIT_PUSH_OPTION_ = "push "
_LINUX_WRITE_COMMAND_ = " > "
_LINUX_WRITE_ERROR_COMMAND_ = " 2> "
_LINUX_PYTHON_COMMAND_ = "python "
_LINUX_PYTHON_M_OPTION_ = "-m "
_LINUX_PYTHON_SITE_OPTION_ = "site "
_LINUX_PYTHON_USER_SITE_OPTION_ = "--user-site "
_LINUX_PIP_COMMAND_ = "pip "
_LINUX_PIP_SHOW_OPTION_ = "show "
_LINUX_ALL_TAG_ = "*"
_LINUX_HEROKU_COMMAND_ = "heroku "
_LINUX_HEROKU_CREATE_OPTION_ = "create "
_LINUX_HEORKU_INFO_OPTION_ = "info "
_LINUX_HEROKU_DESTORY_OPTION_ = "destroy "
_LINUX_HEROKU_DESTROY_CONFIRM_ = " --confirm "
_LINUX_HEROKU_TOKEN_OPTION_ = "auth:token "
_LINUX_HEROKU_LOGIN_OPTION_ = "login "
_LINUX_SNAP_COMMAND_ = "snap "
_LINUX_SNAP_LIST_OPTION_ = "list "
_LINUX_SNAP_INSTALL_OPTION_ = "install "

_FEDORA_DIST_NAME_ = "fedora"
_FEDORA_PACKAGE_MANADER_COMMAND_ = "dnf "

_UBUNTU_DIST_NAME_ = "ubuntu"
_UBUNTU_PACKAGE_MANAGER_COMMAND_ = "apt-get "

_SUPPORT_DIST_ = [_FEDORA_DIST_NAME_, _UBUNTU_DIST_NAME_]

_CRITICAL_ERROR_ = 1
_NORMAL_ERROR_ = 2
