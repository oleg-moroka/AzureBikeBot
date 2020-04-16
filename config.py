#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "58134194-d80c-4854-b5fc-fb0dc7adb917")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "0a38395d-e02c-467d-9a6e-d37967037512")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://bikefaq-service.azurewebsites.net/qnamaker")
    
    