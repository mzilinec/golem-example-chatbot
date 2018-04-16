from golem.core.responses.buttons import LinkButton
from golem.core.responses.responses import TextMessage


def action_root_accept(dialog):
    intent = dialog.context.get("intent", max_age=0)
    # TODO -> YAML examples
    dialog.send_response("Sorry, I don't get it.", "help.root:accept")


def action_help_accept(dialog):
    msg = TextMessage("I can help you remember your stuff. Just tell me what you need to be reminded of and when.")
    msg.add_reply("Remind me to ...")
    dialog.send_response(msg)


def show_about(dialog):
    text = "I am an example chatbot built with the Golem framework at FIT CTU, Prague. " \
           "You can make your own bot quite easily. Check out the source code at GitHub. :)"
    msg = TextMessage(text) \
        .add_button(LinkButton("Golem", "https://github.com/prihoda/golem")) \
        .add_button(LinkButton("FIT CTU", "https://fit.cvut.cz/en"))
    dialog.send_response(msg)


def show_greeting(dialog):
    text = "Hi! I'm a simple bot that can remind you of anything you want."
    msg = TextMessage(text).with_replies(["Remind me ...", "About"])
    dialog.send_response(msg)
