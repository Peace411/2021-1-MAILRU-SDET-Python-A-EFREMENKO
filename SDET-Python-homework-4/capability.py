
import os


def capability_select(download_dir):
    capability = None

    capability = {"platformName": "Android",
                  "platformVersion": "8.1",
                  "automationName": "Appium",
                  "appPackage": "ru.mail.search.electroscope",
                  "appActivity": "ru.mail.search.electroscope.ui.activity.AssistantActivity",
                  "app": os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                      'stuff/Marussia_v1.39.1.apk')
                                         ),
                  "orientation": "PORTRAIT",
                  'autoGrantPermissions': True
                  }
    return capability
