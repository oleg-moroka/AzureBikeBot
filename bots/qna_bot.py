# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount, SuggestedActions, CardAction, ActionTypes

from config import DefaultConfig


class QnABot(ActivityHandler):
    def __init__(self, config: DefaultConfig):
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            )
        )

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Welcome! Ask me about bike selection and different bike features."

                )

    async def on_message_activity(self, turn_context: TurnContext):
        # The actual call to the QnA Maker service.
        response = await self.qna_maker.get_answers(turn_context)
        prompts = response[0].context.prompts

        if response and len(response) > 0:
            reply = MessageFactory.text(response[0].answer)
            if prompts and len(prompts) > 0:
                reply.suggested_actions = SuggestedActions(
                      actions=[
                          CardAction(title = prompts[iter].display_text, type=ActionTypes.im_back, value=prompts[iter].display_text) for iter in range(len(prompts))
                       ]
                      )
            await turn_context.send_activity(reply)
        else:
            await turn_context.send_activity("No QnA Maker answers were found.")
