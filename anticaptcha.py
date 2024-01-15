from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("      ")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

captcha_text = solver.solve_and_return_solution("captcha.png")
if captcha_text != 0:
    print("captcha text " + captcha_text)
else:
    print("task finished with error " + solver.error_code)
