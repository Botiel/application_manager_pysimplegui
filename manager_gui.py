import PySimpleGUI as sg

ENVIRONMENTS = ["test", "stage", "production"]
STATES = ["", "illinois", "ohio", "texas", "indiana"]


class Bot:
    config_checkbox = [["installments - six months", "INSTALLMENTS"], ["headless", "HEADLESS"],
                       ["screenshot", "SCREENSHOT"], ["config file", "BOT_CONFIG"], ["tracing", "TRACING"],
                       ["assert rates", "ASSERT_RATES"]]

    browser = ["chromium", "firefox", "webkit"]
    payment = ["random", "monthly", "automatic", "full"]
    pages = []

    button_events = ["BOT_RUN_BTN", "BOT_SHOW_CONFIG_BTN", "BOT_TRACE_BTN", "BOT_POLICIES_FOLDER_BTN", "BOT_CLEAR_BTN",
                     "BOT_DELETE_PAUSE_BTN", "BOT_INSPECT_BTN", "BOT_ADD_PAUSE_BTN"]

    def __init__(self):
        text_size = (10, 1)
        input_size = (18, 1)
        self.window = None

        data = [

            [sg.Text("Environment:", size=text_size),
             sg.DropDown(values=ENVIRONMENTS, default_value=ENVIRONMENTS[0], size=input_size, key="BOT_ENVIRONMENT")],

            [sg.Text("State:", size=text_size),
             sg.DropDown(values=STATES, default_value=STATES[0], size=input_size, key="BOT_STATES",
                         tooltip=" choose only if you are running a golden standard policy ")],

            [sg.Text("Category:", size=text_size),
             sg.DropDown(values=[], default_value="", size=input_size, key="BOT_CATEGORY")],

            [sg.Text("Policy:", size=text_size),
             sg.DropDown(values=[], default_value="", size=input_size, key="BOT_POLICY")],

            [sg.Text("Payment:", size=text_size),
             sg.DropDown(values=self.payment, default_value=self.payment[0], size=input_size, key="BOT_PAYMENT")],

            [sg.Text("Browser:", size=text_size),
             sg.DropDown(values=self.browser, default_value=self.browser[0], size=input_size, key="BOT_BROWSER")],

            [sg.Text("Date:", size=text_size),
             sg.InputText(size=input_size, key="BOT_DATE",
                          tooltip=" format: MMDDYYYY\n\n"
                                  "- if the policy file has a date the bot will ignore the input\n"
                                  "- if no input and no date in the policy file the bot will calculate"
                                  "\n  a month ahead")]

        ]

        config = [

            [sg.Checkbox(name[0], key=name[1], pad=5)] for name in self.config_checkbox
        ]

        pause = [

            [sg.Text("Page Name:", size=text_size),
             sg.DropDown(values=self.pages, default_value="", size=input_size, key="PAGE_NAME")],

            [sg.Text("")],

            [sg.Button("Add", pad=5, size=10, key="BOT_ADD_PAUSE_BTN"),
             sg.Checkbox("start", pad=5, key="START_PAUSE"), sg.Checkbox("end", pad=5, key="END_PAUSE")],

            [sg.Button("Inspect", pad=5, size=10, key="BOT_INSPECT_BTN")],
            [sg.Button("Delete", pad=5, size=10, tooltip="deleting all pauses", key="BOT_DELETE_PAUSE_BTN")],

            [sg.Text("")]

        ]

        tabs = [[
            sg.TabGroup([[
                sg.Tab("Quote Data", data),
                sg.Tab("Bot Config", config),
                sg.Tab("Add Pause", pause)
            ]])
        ]]

        panel = [

            [sg.Text("")],

            [sg.Button("Run", pad=5, size=12, key="BOT_RUN_BTN")],
            [sg.Button("Show Config", pad=5, size=12, key="BOT_SHOW_CONFIG_BTN")],
            [sg.Button("Trace Viewer", pad=5, size=12, key="BOT_TRACE_BTN")],
            [sg.Button("Policies Folder", pad=5, size=12, key="BOT_POLICIES_FOLDER_BTN")],
            [sg.Button("Clear Display", pad=5, size=12, key="BOT_CLEAR_BTN")]
        ]

        self.layout = [[sg.Frame("", tabs, border_width=0), sg.Frame("", panel, border_width=0)]]

    def create_bot_config(self) -> dict:
        pass

    def create_pause(self) -> dict:
        pass

    def run_quote(self) -> None:
        pass

    def event_loop(self, event: str) -> None:

        for btn_event in self.button_events:
            if btn_event == event:
                print(btn_event, "was clicked")
                break


class Downloader:
    button_events = ["DOWNLOADER_DOWNLOAD_BTN", "DOWNLOADER_CLEAR_BTN", "CONVERT_CONTACT_BTN"]

    def __init__(self):
        text_size = (15, 1)
        input_size = (20, 1)
        self.window = None

        self.layout = [

            [sg.Text("Environment:", size=text_size),
             sg.DropDown(values=ENVIRONMENTS, default_value=ENVIRONMENTS[0],
                         size=input_size, key="DOWNLOADER_ENVIRONMENT")],

            [sg.Text("Opportunity Id:", size=text_size), sg.InputText(
                size=input_size, key="DOWNLOADER_OPPORTUNITY_ID")],

            [sg.Text("File Name:", size=text_size), sg.InputText(size=input_size, key="DOWNLOADER_FILE_NAME")],

            [sg.Text("")],

            [sg.Button("Download", size=(10, 1), key="DOWNLOADER_DOWNLOAD_BTN", pad=5)],

            [sg.Button("Clear Display", size=(10, 1), key="DOWNLOADER_CLEAR_BTN", pad=5)],

            [sg.Text("")],

            [sg.Text("Convert contact to opportunity:", size=(22, 1)),
             sg.InputText(size=input_size, key="CONVERT_CONTACT_INPUT"),
             sg.Button("Convert", size=(10, 1), key="CONVERT_CONTACT_BTN")],

        ]

    def get_download_config(self) -> dict:
        return {
            "environment": self.window["DOWNLOADER_ENVIRONMENT"].get(),
            "id": self.window["DOWNLOADER_OPPORTUNITY_ID"].get(),
            "file_name": self.window["DOWNLOADER_FILE_NAME"].get()
        }

    def download_policy(self) -> None:
        pass

    def convert_contact_to_opportunity(self) -> str:
        pass

    def event_loop(self, event: str) -> None:

        for btn_event in self.button_events:
            if btn_event == event:
                print(btn_event, "was clicked")
                break


class TableCreator:
    button_events = ["CREATOR_CREATE_BTN", "CREATOR_CLEAR_BTN"]

    def __init__(self):
        text_size = (10, 1)
        input_size = (20, 1)
        self.window = None

        self.layout = [

            [sg.Text("Environment:", size=text_size),
             sg.DropDown(values=ENVIRONMENTS, default_value=ENVIRONMENTS[0], size=input_size,
                         key="CREATOR_ENVIRONMENT")],

            [sg.Text("Opportunity Id:", size=text_size), sg.InputText(size=input_size, key="CREATOR_ID")],

            [sg.Text("State:", size=text_size),
             sg.DropDown(values=STATES, default_value=STATES[0], size=input_size, key="CREATOR_STATES")],

            [sg.Text("")],

            [sg.Button("Create Table", size=(10, 1), key="CREATOR_CREATE_BTN", enable_events=True, pad=10)],

            [sg.Button("Clear Display", size=(10, 1), key="CREATOR_CLEAR_BTN", pad=10)]

        ]

    def get_table_config(self) -> dict:
        return {
            "environment": self.window["CREATOR_ENVIRONMENT"].get(),
            "id": self.window["CREATOR_ID"].get(),
            "state": self.window["CREATOR_STATES"].get(),
            "dict": f'rate_log_dictionary_{self.window["CREATOR_ENVIRONMENT"].get()}.xlsx'
        }

    def create_table(self) -> None:
        pass

    def event_loop(self, event: str) -> None:

        for btn_event in self.button_events:
            if btn_event == event:
                print(btn_event, "was clicked")
                break


class DailyTest:
    state_tests = [["Illinois", "IL"], ["Ohio", "OH"], ["Texas", "TX"], ["Indiana", "IN"]]

    other_tests = [["Ezlynx Response Rates", "EZ_RESPONSE"], ["Back To Edit - Ezlynx", "EZ_BTE"],
                   ["Back To Edit - UI", "UI_BTE"]]

    config = [["shell", "SHELL"], ["slack notifications", "SLACK_NOTIFICATIONS"],
              ["upload aws", "UPLOAD_AWS"], ["upload slack", "UPLOAD_SLACK"]]

    button_events = ["DAILY_TEST_LOGIN_BTN", "RUN_DAILY_BTN", "STOP_DAILY_BTN"]

    def __init__(self):
        self.window = None

        tests = [

            [
                sg.Col([[sg.Checkbox(name[0], key=name[1], pad=5)] for name in self.state_tests]),
                sg.Col([[sg.Checkbox(name[0], key=name[1], pad=5)] for name in self.other_tests],
                       vertical_alignment="top")
            ]
        ]

        config = [[sg.Checkbox(text=name[0], key=name[1], pad=5, default=False)] for name in self.config]

        environment = [
            [sg.Radio(text="test", group_id="ENVIRONMENT_GROUP", pad=5, default=True)],
            [sg.Radio(text="stage", group_id="ENVIRONMENT_GROUP", pad=5, default=False)],
            [sg.Radio(text="production", group_id="ENVIRONMENT_GROUP", pad=5, default=False)],
            [sg.Text("", pad=7)]
        ]

        login = [
            [sg.Text("")],

            [sg.Text("Enter Password:", pad=5),
             sg.InputText("", password_char='*', key="ADMIN_PASSWORD", size=(20, 1), pad=5)],

            [sg.Text("")],

            [sg.Push(), sg.Button("Login", size=(10, 1), key="DAILY_TEST_LOGIN_BTN", pad=10), sg.Push()]
        ]

        frames = [
            [sg.Frame("config", config, pad=10), sg.Frame("environment", environment, pad=10, vertical_alignment="top")]
        ]

        tabs = [[
            sg.TabGroup([[
                sg.Tab("Tests", tests),
                sg.Tab("Config", frames),
                sg.Tab("Admin Login", login)
            ]])
        ]]

        buttons = [
            [sg.Text("")],
            [sg.Button("Run", key="RUN_DAILY_BTN", size=(10, 1), pad=5)],
            [sg.Button("Stop", key="STOP_DAILY_BTN", size=(10, 1), pad=5)]
        ]

        self.layout = [
            [sg.Frame("", tabs, border_width=0), sg.Frame("", buttons, border_width=0)]
        ]

    def create_daily_test_config(self) -> dict:
        pass

    def run_daily_tests(self) -> None:
        pass

    def event_loop(self, event: str) -> None:

        for btn_event in self.button_events:
            if btn_event == event:
                print(btn_event, "was clicked")
                break


class DownloadLogs:
    button_events = ["SHOW_LOGS_BTN", "DOWNLOAD_LOGS_BTN"]

    def __init__(self):
        self.window = None
        self.layout = [
            [sg.Text("! Download daily test logs from aws", pad=15)],
            [sg.Text("")],
            [sg.Text("")],
            [sg.Button("Show Logs", size=(13, 1), key="SHOW_LOGS_BTN", pad=15),
             sg.Button("Download Logs", size=(13, 1), key="DOWNLOAD_LOGS_BTN", pad=15),
             sg.InputText(size=(15, 1), key="INPUT_LOGS", tooltip=" Enter log date MMDDYYYY", pad=15)],
        ]

    def download_log(self) -> None:
        pass

    def event_loop(self, event: str) -> None:
        for btn_event in self.button_events:
            if btn_event == event:
                print(btn_event, "was clicked")
                break


class MainApp:

    def __init__(self):

        # ============== SET THEME ==============
        my_new_theme = {'BACKGROUND': '#44475a',
                        'TEXT': '#50fa7b',
                        'INPUT': '#282a36',
                        'TEXT_INPUT': '#50fa7b',
                        'SCROLL': '#c7e78b',
                        'BUTTON': ('#50fa7b', '#282a36'),
                        'PROGRESS': ('#01826B', '#D0D0D0'),
                        'BORDER': 2,
                        'SLIDER_DEPTH': 0,
                        'PROGRESS_DEPTH': 0}
        sg.theme_add_new('nuri', my_new_theme)
        sg.theme('nuri')

        # ================= APPS =================
        self.apps = {
            "BOT": Bot(),
            "DOWNLOAD_POLICY": Downloader(),
            "TABLE_CREATOR": TableCreator(),
            "DAILY_TEST": DailyTest(),
            "DOWNLOAD_LOGS": DownloadLogs()
        }

        # ============== WINDOW VAR ==============
        self.window = None
        self.active_app = None

    def load_layout(self):

        display = [[sg.Output(size=(115, 50), key="DISPLAY")]]

        menu_buttons = [
            [sg.Push(), sg.Text("Menu", pad=15, font=("bold", 12), background_color="#282a36"), sg.Push()],
            [sg.Push(), sg.Button("Bot", size=(13, 1), key="BOT", pad=5), sg.Push()],
            [sg.Push(), sg.Button("Download Policy", size=(13, 1), key="DOWNLOAD_POLICY", pad=5), sg.Push()],
            [sg.Push(), sg.Button("Table Creator", size=(13, 1), key="TABLE_CREATOR", pad=5), sg.Push()],
            [sg.Push(), sg.Button("Daily Test", size=(13, 1), key="DAILY_TEST", pad=5), sg.Push()],
            [sg.Push(), sg.Button("Download Logs", size=(13, 1), key="DOWNLOAD_LOGS", pad=5), sg.Push()],
        ]

        # creating an array of column objects with all the apps layouts.
        # setting visibility to False
        # all apps will be initialized on the same frame spot
        apps = [[sg.Col(v.layout, visible=False, key=f"{k}_COL") for k, v in self.apps.items()]]

        # setting the main layout
        # Frame1 = apps (will rotating between apps) | Frame2 = menu buttons | Frame3 = output display
        layout = [
            [sg.Frame("", apps, size=(440, 270)), sg.Frame("", menu_buttons, size=(360, 270))],
            [sg.Frame("", display, border_width=0)]
        ]

        # ====================================== INITIALIZING MAIN LAYOUT =======================================
        self.window = sg.Window("Sensa Application Manager", layout=layout, size=(800, 700), finalize=True)
        self.window["BOT_COL"].update(visible=True)
        self.active_app = "BOT"

    def switch_app(self, event: str):
        for k, v in self.apps.items():
            if event == k:
                self.window[f"{event}_COL"].update(visible=True)
                v.window = self.window
                self.active_app = event
            else:
                self.window[f"{k}_COL"].update(visible=False)
                v.window = None

    def main_loop(self):

        self.load_layout()

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            # ================ SWITCH APPS =====================
            elif event in list(self.apps):
                self.switch_app(event)

            # ============ACTIVATED APP EVENTS =================
            elif self.active_app in list(self.apps):
                self.apps.get(self.active_app).event_loop(event)

        self.window.close()


if __name__ == '__main__':
    a = MainApp()
    a.main_loop()
