# import streamlit as st
# import requests
# import json


# #credentials

# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"


# st.session_state.transcript = "Upload to get transcript"
# st.session_state.insights = "Upload to get insights"
# st.session_state.callquality = "Upload to get call quality"
# st.session_state.separate = "Upload to get call transcript"
# transcript = "upload"
# quality = "upload"
# insights = "upload"

# t = f"""

# Hello. Hi, may I speak to Anessa Roberts? This is श्री. Good morning Anessa, this is Candus from कृष्ण Telecom. The reason for my call today is about the form you filled out on our website for our fiber plans. Have I caught you at a good time? 
# For now it's fine, but I might be busy soon, but we can talk about it now. 
# Perfect, first I'd like to quickly confirm your address and see if it's part of our serviceable locations. What we have here is one one three four five Keyast Bruce Way, San Antonio, Florida three three five seven six. Is this correct? 
# That's correct. 
# Perfect. So this address is eligible for a fiber connection. We can provide you with the service. Would you like to know more about our available plans? 
# Actually, I was just curious if my location is serviceable for fiber, but I am not really actively looking to switch right now. I am kind of happy with my current provider, so... 
# I understand. This is just going to be a discovery call to see if there are areas we might be able to help you out with. If I could just ask you real quick, how much is the average speed you're getting from your current provider? 
# I'm not sure. I haven't really checked. 
# And what is your current provider? 
# B CNC. 
# And what do you usually use your connection for? Browsing, gaming, streaming? 
# All sorts of things, but mainly just browsing, FaceTime, and streaming most of all. 
# And are you totally happy with how this performs for each of these activities, or do you think it could be better in some aspects? 
# I would say totally happy, but mostly it's acceptable. When watching videos at 4K, there's definitely some lagging. It doesn't matter which device, on our phones or on our TV, it freezes for a few seconds and then resumes. I guess it's the connection because it's definitely not the device. We just bought this 4K TV last month, and it's happening like clockwork every time we watch 4K. Other than that, it's fine.

# """

# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     print("generating access token")
#     auth_url = "https://iam.cloud.ibm.com/identity/token"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Accept": "application/json"
#     }
#     data = {
#         "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
#         "apikey": api_key
#     }
#     response = requests.post(auth_url, headers=headers, data=data)
#     if response.status_code != 200:
#         print(f"Failed to get access token: {response.text}")
#     else:
#         token_info = response.json()
#         # st.write(token_info)
#         return token_info['access_token']


# def Getcallquality(trans):
#     body = {

#     "input":f"""
#     Below is a transcription of a conversation between two people. need call qualtiy ananalysis for given transcription
    

#     The output should look like this:

#     Add-on Request by Customer: customer request...........

#     Action Taken for the request: action taken by ........

#     call rating: rating out of 10

#     Reason: reason for the rating

# Transcription:
#     {trans}

# """,
#     "parameters":{
#         "decoding_method": "greedy",
#         "max_new_tokens": 300,
#         "min_new_tokens": 30,
#         "stop_sequences": [";"],
#         "repetition_penalty": 1.05,
#         "temperature": 0.5
#     },
#     "model_id": model_id,
#     "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#         }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']
#     # st.write(st.session_state.insights)

# def Separatespeakers(trans):
#     body = {

#     "input":f"""
# Below is a transcription of a conversation between two people but it is in parah not seprately. Your task is to separate the conversation into two distinct parts, where one part is for Person1 and the other is for Person2. Each part should contain the dialogue for each speaker. Label the dialogues as follows speaker one and speaker two

# Ensure the dialogues are clearly separated and labeled, maintaining the correct order for each speaker one by one. Separate the conversation based on the order of speech by person one and person two without any explanantion.

# The output should look like this:

# person1: hi

# person2: hi, your name?
# ...

# person1 and person2 will be bold

# Transcription:
# {trans}
# """,
#     "parameters":{
#         "decoding_method": "greedy",
#         "max_new_tokens": 300,
#         "min_new_tokens": 30,
#         "stop_sequences": [";"],
#         "repetition_penalty": 1.05,
#         "temperature": 0.5
#     },
#     "model_id": model_id,
#     "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#         }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.transcript = ""
#     transcript_data = json.dumps(response.json()['results'][0]['generated_text'])
#     st.session_state.separate = json.loads(transcript_data)


# def Getinsights(trans):
#     body = {

#     "input":f"""
# Below is a transcription of a conversation between two people. need insight summary from the given transcription

# The output should look like this:

# Insights Summary: insight summary of the conversation.....

# Sentiment: sentiment of the conversation.....

# i need Insights Summary and Sentiment only

# this is the Transcription:
# {trans}
# """,
#     "parameters":{
#         "decoding_method": "greedy",
#         "max_new_tokens": 300,
#         "min_new_tokens": 30,
#         "stop_sequences": [";"],
#         "repetition_penalty": 1.05,
#         "temperature": 0.5
#     },
#     "model_id": model_id,
#     "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#         }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']
#     # st.write(st.session_state.insights)

# def Gettranscript():
    
#     try:
#         st.write("Uploaded file:", uploaded_file.name)
#         url = "https://dev.assisto.tech/workflow_apis/process_file"
        
#         payload = {}
#         headers = {}
#         files = [('file', (uploaded_file.name, uploaded_file, 'audio/mp3'))]
#         response = requests.request("POST", url, headers=headers, data=payload, files=files)
#         if response.status_code == 200:
#             # st.success("Request sent successfully!")
#                 # st.write(response.json()) 
#             st.session_state.transcript = response.json()['result'][0]['message'] 
 

#             Getinsights(st.session_state.transcript)
#             Getcallquality(st.session_state.transcript)
#             Separatespeakers(st.session_state.transcript)

#         else:
#             st.error(f"Error: {response.status_code} - {response.text}")
#             st.session_state.transcript = response.text
        
#     except requests.exceptions.RequestException as e:
#         st.error(f"An error occurred: {e}")
#         st.session_state.transcript = e

# with top1:
#     st.subheader("Upload Audio")
#     # st.button("Choose File",type="primary",use_container_width=True)
#     uploaded_file = st.file_uploader("Choose File")
#     # if uploaded_file:
#     if st.button("Upload",type="primary",use_container_width=True):
#         Gettranscript()
#         # Getinsights(st.session_state.transcript)
#         # Getcallquality(st.session_state.transcript)
#         # Separatespeakers(st.session_state.transcript)

# with top2:
#     #TRANSCRIPT
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     # st.text_area("",value=st.session_state.transcript,height=300, disabled=True)
#     with st.container(height=200, key=1):
#         st.write(st.session_state.separate)
#     st.markdown("<br>", unsafe_allow_html=True)
#     # st.button("Convert to Text")



# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     # st.write(st.session_state.insights)
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)
#     # if st.button("Generate Insights" ,use_container_width=True):
#     #     Getinsights(st.session_state.transcript)
        

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     # st.write(st.session_state.callquality)
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)
#     # st.button("Call quality analysis",use_container_width=True)


# import streamlit as st
# import requests
# import json
# import ibm_boto3
# from ibm_botocore.client import Config
# import io
# import base64  # For handling base64-encoded audio if present in JSON

# # IBM COS Credentials
# COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
# COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
# COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
# COS_BUCKET = "ozonetell"

# # Initialize COS client
# cos_client = ibm_boto3.client(
#     's3',
#     ibm_api_key_id=COS_API_KEY,
#     ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
#     config=Config(signature_version='oauth'),
#     endpoint_url=COS_ENDPOINT
# )

# # Existing API credentials for Watsonx
# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"

# # Session state initialization
# st.session_state.transcript = "Select a JSON file to get transcript"
# st.session_state.insights = "Select a JSON file to get insights"
# st.session_state.callquality = "Select a JSON file to get call quality"
# st.session_state.separate = "Select a JSON file to get call transcript"

# # Page config
# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
#     data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
#     response = requests.post(auth_url, headers=headers, data=data)
#     return response.json()['access_token']

# def Getcallquality(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. need call qualtiy ananalysis for given transcription
#         The output should look like this:
#         Add-on Request by Customer: customer request...........
#         Action Taken for the request: action taken by ........
#         call rating: rating out of 10
#         Reason: reason for the rating
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']

# def Separatespeakers(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people but it is in parah not seprately. Your task is to separate the conversation into two distinct parts, where one part is for Person1 and the other is for Person2. Each part should contain the dialogue for each speaker. Label the dialogues as follows speaker one and speaker two
#         Ensure the dialogues are clearly separated and labeled, maintaining the correct order for each speaker one by one. Separate the conversation based on the order of speech by person one and person two without any explanantion.
#         The output should look like this:
#         person1: hi
#         person2: hi, your name?
#         ...
#         person1 and person2 will be bold
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.transcript = ""
#     transcript_data = json.dumps(response.json()['results'][0]['generated_text'])
#     st.session_state.separate = json.loads(transcript_data)

# def Getinsights(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. need insight summary from the given transcription
#         The output should look like this:
#         Insights Summary: insight summary of the conversation.....
#         Sentiment: sentiment of the conversation.....
#         i need Insights Summary and Sentiment only
#         this is the Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']

# def get_cos_files():
#     """Fetch list of JSON files from COS with debugging"""
#     try:
#         st.write("Attempting to list objects in bucket:", COS_BUCKET)
#         response = cos_client.list_objects_v2(Bucket=COS_BUCKET)
#         st.write("API Response received. Number of objects:", len(response.get('Contents', [])))
#         files = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.json')]
#         if not files:
#             st.warning("No .json files found in the bucket 'ozonetell'. Please ensure JSON files are uploaded.")
#         else:
#             st.write("Found JSON files:", files)
#         return files
#     except Exception as e:
#         st.error(f"Error fetching COS files: {e}")
#         return []

# def process_audio_from_cos(file_key):
#     try:
#         st.write(f"Processing JSON file: {file_key}")
#         # Download JSON file from COS
#         file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
#         json_data = json.loads(file_obj['Body'].read().decode('utf-8'))
        
#         # Assuming JSON contains base64-encoded audio (adjust based on your JSON structure)
#         if 'audio' in json_data and 'data' in json_data['audio']:  # Example structure
#             audio_base64 = json_data['audio']['data']
#             audio_bytes = base64.b64decode(audio_base64)
#         else:
#             st.error("Unsupported JSON format. Please provide a sample JSON structure.")
#             return

#         # Prepare file for API
#         url = "https://dev.assisto.tech/workflow_apis/process_file"
#         payload = {}
#         files = [('file', (file_key, io.BytesIO(audio_bytes), 'audio/mpeg'))]
#         headers = {}
        
#         response = requests.post(url, headers=headers, data=payload, files=files)
#         if response.status_code == 200:
#             st.session_state.transcript = response.json()['result'][0]['message']
#             Getinsights(st.session_state.transcript)
#             Getcallquality(st.session_state.transcript)
#             Separatespeakers(st.session_state.transcript)
#         else:
#             st.error(f"Error from external API: {response.status_code} - {response.text}")
#             st.session_state.transcript = response.text
#     except Exception as e:
#         st.error(f"An error occurred while processing the file: {e}")
#         st.session_state.transcript = str(e)

# with top1:
#     st.subheader("Select JSON from IBM COS")
#     json_files = get_cos_files()
#     selected_file = st.selectbox("Choose a JSON file", json_files)
#     if st.button("Process Audio", type="primary", use_container_width=True) and selected_file:
#         process_audio_from_cos(selected_file)

# with top2:
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     with st.container(height=200, key=1):
#         st.write(st.session_state.separate)

# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)


# import streamlit as st
# import requests
# import json
# import ibm_boto3
# from ibm_botocore.client import Config
# import io

# # IBM COS Credentials
# COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
# COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
# COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
# COS_BUCKET = "ozonetell"

# # Initialize COS client
# cos_client = ibm_boto3.client(
#     's3',
#     ibm_api_key_id=COS_API_KEY,
#     ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
#     config=Config(signature_version='oauth'),
#     endpoint_url=COS_ENDPOINT
# )

# # Existing API credentials for Watsonx
# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"

# # Session state initialization
# st.session_state.transcript = "Select a JSON file to get transcript"
# st.session_state.insights = "Select a JSON file to get insights"
# st.session_state.callquality = "Select a JSON file to get call quality"
# st.session_state.separate = "Select a JSON file to get call transcript"
# st.session_state.raw_transcript = "Raw transcript will appear here"

# # Page config
# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0e1117;
#     }
#     .css-1d8v1u7, .css-1a32f9v {
#         color: #ffffff !important; /* Bright white text to match other boxes */
#         font-size: 16px !important; /* Consistent text size */
#     }
#     </style>
# """, unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
#     data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
#     response = requests.post(auth_url, headers=headers, data=data)
#     return response.json()['access_token']

# def Getcallquality(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need call quality analysis for the given transcription.
#         The output should look like this:
#         Add-on Request by Customer: customer request...........
#         Action Taken for the request: action taken by ........
#         call rating: rating out of 10
#         Reason: reason for the rating
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']

# def Getinsights(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need insight summary from the given transcription.
#         The output should look like this:
#         Insights Summary: insight summary of the conversation.....
#         Sentiment: sentiment of the conversation.....
#         I need Insights Summary and Sentiment only.
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']

# def Separatespeakers(trans):
#     prompt = f"""
#     Below is a transcription of a conversation between two people, presented in paragraph form and not separated. Your task is to accurately separate the conversation into two distinct parts, one for each speaker, based on the order of speech. Label the speakers as **Person1** and **Person2** for the first and second speakers respectively, alternating based on the sequence. Do not assume specific roles (e.g., agent or customer); rely solely on the order of dialogue, natural flow, and contextual cues such as questions, responses, or pauses to determine speaker turns. Exclude the raw transcript or any extra labels from the output—provide only the separated dialogue with **Person1** and **Person2** labels.

#     Provide detailed examples to guide your separation:
#     - If a speaker initiates with a question or request (e.g., "Can you verify the items?"), assign it to Person1, and if the next part responds (e.g., "Of course, let me check..."), assign it to Person2.
#     - Use pauses (e.g., "(pause)") as indicators to confirm speaker switches where applicable.
#     - Ensure each speaker’s full dialogue is grouped together as a single turn before switching to the next speaker, starting Person2 on a new line after Person1’s complete turn. Do not split a speaker’s turn or include the raw transcript text.

#     The output should use bold text for speaker labels (**Person1**: ...) followed by their dialogue on the same line. Maintain the original wording, punctuation, and formatting (e.g., pauses in parentheses). Achieve 100% accuracy by carefully analyzing the dialogue flow, ensuring no speaker’s turn is misassigned or mixed with raw transcript text.

#     Transcription:
#     {trans}
#     """
#     body = {
#         "input": prompt,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 500,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.separate = response.json()['results'][0]['generated_text']

# def get_cos_files():
#     try:
#         st.write("Attempting to list objects in bucket:", COS_BUCKET)
#         response = cos_client.list_objects_v2(Bucket=COS_BUCKET)
#         st.write("API Response received. Number of objects:", len(response.get('Contents', [])))
#         files = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.json')]
#         if not files:
#             st.warning("No .json files found in the bucket 'ozonetell'. Please ensure JSON files are uploaded.")
#         else:
#             st.write("Found JSON files:", files)
#         return files
#     except Exception as e:
#         st.error(f"Error fetching COS files: {e}")
#         return []

# def process_audio_from_cos(file_key):
#     try:
#         st.write(f"Processing JSON file: {file_key}")
#         file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
#         json_data = json.loads(file_obj['Body'].read().decode('utf-8'))
        
#         if 'AudioFile' in json_data:
#             audio_url = json_data['AudioFile']
#             st.write(f"Downloading audio from: {audio_url}")
            
#             audio_response = requests.get(audio_url, stream=True)
#             if audio_response.status_code == 200:
#                 audio_data = audio_response.content
#             else:
#                 st.error(f"Failed to download audio from {audio_url}. Status code: {audio_response.status_code}")
#                 return
#         else:
#             st.error("No 'AudioFile' field found in JSON. Please check the JSON structure.")
#             return

#         url = "https://dev.assisto.tech/workflow_apis/process_file"
#         payload = {}
#         files = [('file', (file_key, io.BytesIO(audio_data), 'audio/mpeg'))]
#         headers = {}
        
#         response = requests.post(url, headers=headers, data=payload, files=files)
#         if response.status_code == 200:
#             transcript = response.json()['result'][0]['message']
#             st.session_state.raw_transcript = transcript
#             st.session_state.transcript = transcript
#             Getinsights(st.session_state.transcript)
#             Getcallquality(st.session_state.transcript)
#             Separatespeakers(st.session_state.transcript)
#         else:
#             st.error(f"Error from external API: {response.status_code} - {response.text}")
#             st.session_state.transcript = response.text
#     except Exception as e:
#         st.error(f"An error occurred while processing the file: {e}")
#         st.session_state.transcript = str(e)

# # Layout
# with top1:
#     st.subheader("Select Audio from IBM COS")
#     json_files = get_cos_files()
#     selected_file = st.selectbox("Choose an audio file", json_files, placeholder="No options to select.")
#     if st.button("Process Audio", type="primary", use_container_width=True) and selected_file:
#         process_audio_from_cos(selected_file)

# with top2:
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     with st.container(height=300):
#         if st.session_state.transcript == "Select a JSON file to get transcript":
#             st.write("Transcript will appear here")
#         else:
#             st.subheader("Transcript")
#             st.write(st.session_state.raw_transcript)
#             st.write(st.session_state.separate)

# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)

# import streamlit as st
# import requests
# import json
# import ibm_boto3
# from ibm_botocore.client import Config
# import io

# # IBM COS Credentials
# COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
# COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
# COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
# COS_BUCKET = "ozonetell"

# # Initialize COS client
# cos_client = ibm_boto3.client(
#     's3',
#     ibm_api_key_id=COS_API_KEY,
#     ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
#     config=Config(signature_version='oauth'),
#     endpoint_url=COS_ENDPOINT
# )

# # Existing API credentials for Watsonx
# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"

# # Session state initialization
# st.session_state.transcript = "Select a JSON file to get transcript"
# st.session_state.insights = "Select a JSON file to get insights"
# st.session_state.callquality = "Select a JSON file to get call quality"
# st.session_state.separate = "Select a JSON file to get call transcript"
# st.session_state.raw_transcript = "Raw transcript will appear here"

# # Page config
# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0e1117;
#     }
#     .css-1d8v1u7, .css-1a32f9v {
#         color: #ffffff !important; /* Bright white text to match other boxes */
#         font-size: 16px !important; /* Consistent text size */
#     }
#     </style>
# """, unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
#     data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
#     response = requests.post(auth_url, headers=headers, data=data)
#     return response.json()['access_token']

# def Getcallquality(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need call quality analysis for the given transcription.
#         The output should look like this:
#         Add-on Request by Customer: customer request...........
#         Action Taken for the request: action taken by ........
#         call rating: rating out of 10
#         Reason: reason for the rating
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']

# def Getinsights(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need insight summary from the given transcription.
#         The output should look like this:
#         Insights Summary: insight summary of the conversation.....
#         Sentiment: sentiment of the conversation.....
#         I need Insights Summary and Sentiment only.
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']

# def Separatespeakers(trans):
#     prompt = f"""
#     Below is a transcription of a conversation between two people, presented in paragraph form and not separated. Your task is to accurately separate the conversation into two distinct parts, one for each speaker, based on the order of speech. Label the speakers as **Person1** and **Person2** for the first and second speakers respectively, alternating based on the sequence. Do not assume specific roles (e.g., agent or customer); rely solely on the order of dialogue, natural flow, and contextual cues such as questions, responses, or pauses to determine speaker turns. Exclude the raw transcript or any extra labels from the output—provide only the separated dialogue with **Person1** and **Person2** labels.

#     Provide detailed examples to guide your separation:
#     - If a speaker initiates with a question or request (e.g., "Can you verify the items?"), assign it to Person1, and if the next part responds (e.g., "Of course, let me check..."), assign it to Person2.
#     - Use pauses (e.g., "(pause)") as indicators to confirm speaker switches where applicable.
#     - Ensure each speaker’s full dialogue is grouped together as a single turn before switching to the next speaker, starting Person2 on a new line after Person1’s complete turn. Do not split a speaker’s turn or include the raw transcript text.

#     The output should use bold text for speaker labels (**Person1**: ...) followed by their dialogue on the same line. Maintain the original wording, punctuation, and formatting (e.g., pauses in parentheses). Achieve 100% accuracy by carefully analyzing the dialogue flow, ensuring no speaker’s turn is misassigned or mixed with raw transcript text.

#     Transcription:
#     {trans}
#     """
#     body = {
#         "input": prompt,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 500,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.separate = response.json()['results'][0]['generated_text']

# def get_cos_files():
#     try:
#         response = cos_client.list_objects_v2(Bucket=COS_BUCKET)
#         files = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.json')]
#         if not files:
#             st.warning("No .json files found in the bucket 'ozonetell'. Please ensure JSON files are uploaded.")
#         return files
#     except Exception as e:
#         st.error(f"Error fetching COS files: {e}")
#         return []

# def process_audio_from_cos(file_key):
#     try:
#         file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
#         json_data = json.loads(file_obj['Body'].read().decode('utf-8'))
        
#         if 'AudioFile' in json_data:
#             audio_url = json_data['AudioFile']
            
#             audio_response = requests.get(audio_url, stream=True)
#             if audio_response.status_code == 200:
#                 audio_data = audio_response.content
#             else:
#                 st.error(f"Failed to download audio from {audio_url}. Status code: {audio_response.status_code}")
#                 return
#         else:
#             st.error("No 'AudioFile' field found in JSON. Please check the JSON structure.")
#             return

#         url = "https://dev.assisto.tech/workflow_apis/process_file"
#         payload = {}
#         files = [('file', (file_key, io.BytesIO(audio_data), 'audio/mpeg'))]
#         headers = {}
        
#         response = requests.post(url, headers=headers, data=payload, files=files)
#         if response.status_code == 200:
#             transcript = response.json()['result'][0]['message']
#             st.session_state.raw_transcript = transcript
#             st.session_state.transcript = transcript
#             Getinsights(st.session_state.transcript)
#             Getcallquality(st.session_state.transcript)
#             Separatespeakers(st.session_state.transcript)
#         else:
#             st.error(f"Error from external API: {response.status_code} - {response.text}")
#             st.session_state.transcript = response.text
#     except Exception as e:
#         st.error(f"An error occurred while processing the file: {e}")
#         st.session_state.transcript = str(e)

# # Layout
# with top1:
#     st.subheader("Select Audio from IBM COS")
#     json_files = get_cos_files()
#     selected_file = st.selectbox("Choose an audio file", json_files, placeholder="No options to select.")
#     if st.button("Process Audio", type="primary", use_container_width=True) and selected_file:
#         process_audio_from_cos(selected_file)

# with top2:
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     with st.container(height=300):
#         if st.session_state.transcript == "Select a JSON file to get transcript":
#             st.write("Transcript will appear here")
#         else:
#             st.subheader("Transcript")
#             st.write(st.session_state.raw_transcript)
#             st.write(st.session_state.separate)

# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)

#JSON File Conversion Transcription Processing.
import streamlit as st
import requests
import json
import ibm_boto3
from ibm_botocore.client import Config
import io
import urllib.parse

# IBM COS Credentials
COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
COS_BUCKET = "ozonetell"

# Initialize COS client
cos_client = ibm_boto3.client(
    's3',
    ibm_api_key_id=COS_API_KEY,
    ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
    config=Config(signature_version='oauth'),
    endpoint_url=COS_ENDPOINT
)

# Existing API credentials for Watsonx
api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
model_id = "meta-llama/llama-3-2-90b-vision-instruct"
auth_url = "https://iam.cloud.ibm.com/identity/token"

# Session state initialization
st.session_state.transcript = "Select a JSON file to get transcript"
st.session_state.insights = "Select a JSON file to get insights"
st.session_state.callquality = "Select a JSON file to get call quality"
st.session_state.separate = "Select a JSON file to get call transcript"
st.session_state.raw_transcript = "Raw transcript will appear here"
st.session_state.failed_files = []  # To track files with invalid AudioFile

# Page config
st.set_page_config(layout="wide", page_title="Wave Infra Call Insights")
st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights</h1>", unsafe_allow_html=True)
st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .css-1d8v1u7, .css-1a32f9v {
        color: #ffffff !important; /* Bright white text to match other boxes */
        font-size: 16px !important; /* Consistent text size */
    }
    </style>
""", unsafe_allow_html=True)

top1, top2 = st.columns(2)
bottom1, bottom2 = st.columns(2)

def access_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
    data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
    response = requests.post(auth_url, headers=headers, data=data)
    return response.json()['access_token']

def Getcallquality(trans):
    print(trans)
    body = {
        "input": f"""
        Below is a transcription of a conversation between two people. Need call quality analysis for the given transcription.
        The output should look like this:
        Add-on Request by Customer: customer request...........
        Action Taken for the request: action taken by ........
        call rating: rating out of 10
        Reason: reason for the rating
        Transcription:
        {trans}
        """,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 300,
            "min_new_tokens": 30,
            "stop_sequences": [";"],
            "repetition_penalty": 1.05,
            "temperature": 0.5
        },
        "model_id": model_id,
        "project_id": project_id
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token()}"
    }
    response = requests.post(url, headers=headers, json=body)
    st.session_state.callquality = response.json()['results'][0]['generated_text']

def Getinsights(trans):
    print(trans)
    body = {
        "input": f"""
        Below is a transcription of a conversation between two people. Need insight summary from the given transcription.
        The output should look like this:
        Insights Summary: insight summary of the conversation.....
        Sentiment: sentiment of the conversation.....
        I need Insights Summary and Sentiment only.
        Transcription:
        {trans}
        """,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 300,
            "min_new_tokens": 30,
            "stop_sequences": [";"],
            "repetition_penalty": 1.05,
            "temperature": 0.5
        },
        "model_id": model_id,
        "project_id": project_id
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token()}"
    }
    response = requests.post(url, headers=headers, json=body)
    st.session_state.insights = response.json()['results'][0]['generated_text']

def Separatespeakers(trans):
    # print(trans)
    prompt = f"""
    You are a conversation formatter. 
    
    I'm going to give you a raw call transcript. Convert it into a clean conversation format where each turn is clearly labeled as either "Speaker1:" or "Speaker2:" (no bold, no asterisks).
    
    Each speaker should be on a new line. Make sure to preserve the natural flow of conversation, with questions followed by answers and logical turn-taking.
    
    Here is the transcript:
    {trans}
    
    Format your response exactly like this example:
    Speaker1: [First speaker's text]
    Speaker2: [Second speaker's text]
    Speaker1: [First speaker's next turn]
    Speaker2: [Second speaker's response]


    Important: ONLY output the formatted conversation. Do not include any explanations, headers, or notes.
    """
    
    body = {
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 1000,
            "min_new_tokens": 30,
            "repetition_penalty": 1.05,
            "temperature": 0.1
        },
        "model_id": model_id,
        "project_id": project_id
    }
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token()}"
    }
    
    response = requests.post(url, headers=headers, json=body)
    response_text = response.json()['results'][0]['generated_text']
    
    # Additional processing to ensure proper formatting
    lines = response_text.split('\n')
    clean_lines = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines or explanatory text
        if not line or "transcript" in line.lower() or "conversation" in line.lower():
            continue
            
        # Check for various formats and standardize
        if line.startswith('Speaker1:') or line.startswith('Speaker2:'):
            clean_lines.append(line)

        elif line.startswith('Speaker 1:'):
            clean_lines.append(line.replace('Speaker 1:', 'Speaker1:'))
        elif line.startswith('Speaker 2:'):
            clean_lines.append(line.replace('Speaker 2:', 'Speaker2:'))
        elif line.startswith('**Speaker1**:'):
            clean_lines.append(line.replace('**Speaker1**:', 'Speaker1:'))
        elif line.startswith('**Speaker2**:'):
            clean_lines.append(line.replace('**Speaker2**:', 'Speaker2:'))
        elif line.startswith('**Speaker 1**:'):
            clean_lines.append(line.replace('**Speaker 1**:', 'Speaker1:'))
        elif line.startswith('**Speaker 2**:'):
            clean_lines.append(line.replace('**Speaker 2**:', 'Speaker2:'))
    
    # Return the clean, formatted output
    if clean_lines:
        st.session_state.separate = '\n'.join(clean_lines)
    else:
        # If no properly formatted lines are found, use a simple approach
        # Split by sentences and alternate speakers
        sentences = trans.split('.')
        alternate_lines = []
        is_speaker1 = True
        
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                speaker = "Speaker1" if is_speaker1 else "Speaker2"
                alternate_lines.append(f"{speaker}: {sentence}.")
                is_speaker1 = not is_speaker1
        
        st.session_state.separate = '\n'.join(alternate_lines)
def get_cos_files():
    try:
        response = cos_client.list_objects_v2(Bucket=COS_BUCKET)
        files = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.json')]
        if not files:
            st.warning("No .json files found in the bucket 'ozonetell'. Please ensure JSON files are uploaded.")
        return files
    except Exception as e:
        st.error(f"Error fetching COS files: {e}")
        return []

def process_audio_from_cos(file_key):
    try:
        file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
        json_data = json.loads(file_obj['Body'].read().decode('utf-8'))
        
        # Debug: Display the raw JSON content
        st.write("Raw JSON content for", file_key + ":", json.dumps(json_data, indent=2))
        
        if 'AudioFile' not in json_data or not json_data['AudioFile']:
            st.error(f"No valid 'AudioFile' URL found in {file_key}. Adding to failed files list for review.")
            st.session_state.failed_files.append(file_key)
            return

        audio_url = json_data['AudioFile']
        # Validate that the URL has a scheme (e.g., https://)
        result = urllib.parse.urlparse(audio_url)
        if not result.scheme:
            st.error(f"Invalid URL '{audio_url}' in {file_key}: No scheme supplied. Perhaps you meant https://{audio_url}? Adding to failed files list for review.")
            st.session_state.failed_files.append(file_key)
            return

        audio_response = requests.get(audio_url, stream=True)
        if audio_response.status_code == 200:
            audio_data = audio_response.content
        else:
            st.error(f"Failed to download audio from {audio_url} in {file_key}. Status code: {audio_response.status_code}")
            st.session_state.failed_files.append(file_key)
            return

        url = "https://dev.assisto.tech/workflow_apis/process_file"
        payload = {}
        files = [('file', (file_key, io.BytesIO(audio_data), 'audio/mpeg'))]
        headers = {}
        
        response = requests.post(url, headers=headers, data=payload, files=files)
        if response.status_code == 200:
            transcript = response.json()['result'][0]['message']
            st.session_state.raw_transcript = transcript
            st.session_state.transcript = transcript
            # print("ithu naa print pannathu")
            # print(st.session_state.transcript)
            Getinsights(st.session_state.transcript)
            Getcallquality(st.session_state.transcript)
            Separatespeakers(st.session_state.transcript)
        else:
            st.error(f"Error from external API for {file_key}: {response.status_code} - {response.text}")
            st.session_state.transcript = response.text
    except Exception as e:
        st.error(f"An error occurred while processing the file {file_key}: {e}")
        st.session_state.transcript = str(e)

# Layout
with top1:
    st.subheader("Select Audio from IBM COS")
    json_files = get_cos_files()
    selected_file = st.selectbox("Choose an audio file", json_files, placeholder="No options to select.")
    if st.button("Process Audio", type="primary", use_container_width=True) and selected_file:
        process_audio_from_cos(selected_file)
    # Display failed files if any
    if st.session_state.failed_files:
        st.warning(f"The following files failed due to invalid 'AudioFile' URLs: {st.session_state.failed_files}")
        st.write("Please update these JSON files to include a valid 'AudioFile' key with a URL (e.g., https://example.com/audio.mp3).")

with top2:
    st.subheader("Call Transcript using Watsonx Speech-To-text")
    with st.container(height=300):
        if st.session_state.separate == "Select a JSON file to get call transcript":
            st.write("Transcript will appear here")
        else:
            st.write(st.session_state.separate)  # Only show the formatted Speaker1/Speaker2 output

with bottom1:
    st.subheader("Call Insights by watsonx.ai")
    with st.container(height=300, key=2):
        st.write(st.session_state.insights)

with bottom2:
    st.subheader("Call quality analysis by watsonx.ai")
    with st.container(height=300, key=3):
        st.write(st.session_state.callquality)
#MP3 File Upload and Transcription
# import streamlit as st
# import requests
# import json
# import ibm_boto3
# from ibm_botocore.client import Config
# import io
# import urllib.parse

# # IBM COS Credentials
# COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
# COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
# COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
# COS_BUCKET = "ozonetell"

# # Initialize COS client
# cos_client = ibm_boto3.client(
#     's3',
#     ibm_api_key_id=COS_API_KEY,
#     ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
#     config=Config(signature_version='oauth'),
#     endpoint_url=COS_ENDPOINT
# )

# # Existing API credentials for Watsonx
# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"

# # Session state initialization
# st.session_state.transcript = "Select an MP3 file to get transcript"
# st.session_state.insights = "Select an MP3 file to get insights"
# st.session_state.callquality = "Select an MP3 file to get call quality"
# st.session_state.separate = "Select an MP3 file to get call transcript"
# st.session_state.raw_transcript = "Raw transcript will appear here"
# st.session_state.failed_files = []  # Track files with issues

# # Page config
# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0e1117;
#     }
#     .css-1d8v1u7, .css-1a32f9v {
#         color: #ffffff !important; /* Bright white text to match other boxes */
#         font-size: 16px !important; /* Consistent text size */
#     }
#     </style>
# """, unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
#     data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
#     response = requests.post(auth_url, headers=headers, data=data)
#     return response.json()['access_token']

# def Getcallquality(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need call quality analysis for the given transcription.
#         The output should look like this:
#         Add-on Request by Customer: customer request...........
#         Action Taken for the request: action taken by ........
#         call rating: rating out of 10
#         Reason: reason for the rating
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']

# def Getinsights(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need insight summary from the given transcription.
#         The output should look like this:
#         Insights Summary: insight summary of the conversation.....
#         Sentiment: sentiment of the conversation.....
#         I need Insights Summary and Sentiment only.
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']

# def Separatespeakers(trans):
#     prompt = f"""
#     Below is a transcription of a conversation between two people, presented in paragraph form and not separated. Your task is to accurately separate the conversation into two distinct parts, one for each speaker, based on the order of speech. Label the speakers as **Person1** and **Person2** for the first and second speakers respectively, alternating based on the sequence. Do not assume specific roles (e.g., agent or customer); rely solely on the order of dialogue, natural flow, and contextual cues such as questions, responses, or pauses to determine speaker turns. Exclude the raw transcript or any extra labels from the output—provide only the separated dialogue with **Person1** and **Person2** labels.

#     Provide detailed examples to guide your separation:
#     - If a speaker initiates with a question or request (e.g., "Can you verify the items?"), assign it to Person1, and if the next part responds (e.g., "Of course, let me check..."), assign it to Person2.
#     - Use pauses (e.g., "(pause)") as indicators to confirm speaker switches where applicable.
#     - Ensure each speaker’s full dialogue is grouped together as a single turn before switching to the next speaker, starting Person2 on a new line after Person1’s complete turn. Do not split a speaker’s turn or include the raw transcript text.

#     The output should use bold text for speaker labels (**Person1**: ...) followed by their dialogue on the same line. Maintain the original wording, punctuation, and formatting (e.g., pauses in parentheses). Achieve 100% accuracy by carefully analyzing the dialogue flow, ensuring no speaker’s turn is misassigned or mixed with raw transcript text.

#     Transcription:
#     {trans}
#     """
#     body = {
#         "input": prompt,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 500,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.separate = response.json()['results'][0]['generated_text']

# def get_cos_files():
#     try:
#         all_files = []
#         continuation_token = None
#         while True:
#             params = {
#                 'Bucket': COS_BUCKET,
#                 'MaxKeys': 1000
#             }
#             if continuation_token:
#                 params['ContinuationToken'] = continuation_token
#             response = cos_client.list_objects_v2(**params)
#             st.write("Raw COS response (page):", response)  # Debug: Show each page response
#             contents = response.get('Contents', [])
#             if not contents:
#                 st.warning("No objects found in this page. Checking next page if available.")
#             files = [obj['Key'] for obj in contents if obj['Key'].lower().endswith('.mp3')]
#             all_files.extend(files)
#             if not response.get('IsTruncated'):
#                 break
#             continuation_token = response.get('NextContinuationToken')
#         if not all_files:
#             st.warning("No .mp3 files found in the bucket 'ozonetell' after pagination. Please ensure MP3 files are uploaded.")
#         return all_files
#     except Exception as e:
#         st.error(f"Error fetching COS files: {e}")
#         return []

# def process_audio_from_cos(file_key):
#     try:
#         # Directly get the MP3 file content
#         file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
#         audio_data = file_obj['Body'].read()
        
#         # Debug: Note the file being processed
#         st.write(f"Processing MP3 file: {file_key}")
        
#         url = "https://dev.assisto.tech/workflow_apis/process_file"
#         payload = {}
#         files = [('file', (file_key, io.BytesIO(audio_data), 'audio/mpeg'))]
#         headers = {}
        
#         response = requests.post(url, headers=headers, data=payload, files=files)
#         if response.status_code == 200:
#             transcript = response.json()['result'][0]['message']
#             st.session_state.raw_transcript = transcript
#             st.session_state.transcript = transcript
#             Getinsights(st.session_state.transcript)
#             Getcallquality(st.session_state.transcript)
#             Separatespeakers(st.session_state.transcript)
#         else:
#             st.error(f"Error from external API for {file_key}: {response.status_code} - {response.text}")
#             st.session_state.transcript = response.text
#             st.session_state.failed_files.append(file_key)
#     except Exception as e:
#         st.error(f"An error occurred while processing the file {file_key}: {e}")
#         st.session_state.transcript = str(e)
#         st.session_state.failed_files.append(file_key)

# # Layout
# with top1:
#     st.subheader("Select Audio from IBM COS")
#     mp3_files = get_cos_files()
#     selected_file = st.selectbox("Choose an MP3 file", mp3_files, placeholder="No options to select.")
#     if st.button("Process Audio", type="primary", use_container_width=True) and selected_file:
#         process_audio_from_cos(selected_file)
#     # Display failed files if any
#     if st.session_state.failed_files:
#         st.warning(f"The following files failed due to processing issues: {st.session_state.failed_files}")
#         st.write("Please verify these MP3 files or check the external API.")

# with top2:
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     with st.container(height=300):
#         if st.session_state.transcript == "Select an MP3 file to get transcript":
#             st.write("Transcript will appear here")
#         else:
#             st.subheader("Transcript")
#             st.write(st.session_state.raw_transcript)
#             st.write(st.session_state.separate)

# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)

#Automation Working Script
# import streamlit as st
# import requests
# import json
# import ibm_boto3
# from ibm_botocore.client import Config
# import io
# import urllib.parse
# from datetime import datetime

# # IBM COS Credentials
# COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
# COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
# COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
# COS_BUCKET = "ozonetell"

# # Initialize COS client
# cos_client = ibm_boto3.client(
#     's3',
#     ibm_api_key_id=COS_API_KEY,
#     ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
#     config=Config(signature_version='oauth'),
#     endpoint_url=COS_ENDPOINT
# )

# # Existing API credentials for Watsonx
# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"

# # Salesforce Credentials
# SALESFORCE_CLIENT_ID = "3MVG9wt4IL4O5wvKmuWykzw13DGFOnjtd2q0MhKTvjQRdylQtrxmuTnEq4i2_.s6sQSQ5YJMl.1n_ScCpSDSP"
# SALESFORCE_CLIENT_SECRET = "B7143F5B5BEA70B22F037608F6FDCD818AFEFDC88CD1588FB0608720471E9369"
# SALESFORCE_USERNAME = "impwatson@gadieltechnologies.com"
# SALESFORCE_PASSWORD = "Wave@#123456"
# SALESFORCE_TOKEN_URL = "https://login.salesforce.com/services/oauth2/token"
# SALESFORCE_INSTANCE_URL = "https://waveinfratech.my.salesforce.com"
# SALESFORCE_API_VERSION = "v58.0"

# # Session state initialization
# if 'last_processed_file' not in st.session_state:
#     st.session_state.last_processed_file = None
# st.session_state.transcript = "Select a JSON file to get transcript"
# st.session_state.insights = "Select a JSON file to get insights"
# st.session_state.callquality = "Select a JSON file to get call quality"
# st.session_state.separate = "Select a JSON file to get call transcript"
# st.session_state.raw_transcript = "Raw transcript will appear here"
# st.session_state.failed_files = []  # To track files with invalid AudioFile

# # Page config
# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0e1117;
#     }
#     .css-1d8v1u7, .css-1a32f9v {
#         color: #ffffff !important; /* Bright white text to match other boxes */
#         font-size: 16px !important; /* Consistent text size */
#     }
#     </style>
# """, unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
#     data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
#     response = requests.post(auth_url, headers=headers, data=data)
#     return response.json()['access_token']

# def get_salesforce_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}
#     data = {
#         "grant_type": "password",
#         "client_id": SALESFORCE_CLIENT_ID,
#         "client_secret": SALESFORCE_CLIENT_SECRET,
#         "username": SALESFORCE_USERNAME,
#         "password": SALESFORCE_PASSWORD
#     }
#     response = requests.post(SALESFORCE_TOKEN_URL, headers=headers, data=data)
#     if response.status_code == 200:
#         return response.json()['access_token']
#     else:
#         st.error(f"Failed to get Salesforce token: {response.text}")
#         return None

# def push_to_salesforce(transcript, insights, callquality, separate):
#     access_token = get_salesforce_token()
#     if not access_token:
#         return

#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     report_data = {
#         "Transcript": transcript,
#         "Insights": insights,
#         "CallQuality": callquality,
#         "SeparatedSpeakers": separate
#     }
#     api_endpoint = f"{SALESFORCE_INSTANCE_URL}/services/data/{SALESFORCE_API_VERSION}/sobjects/Call_Report__c/"
#     response = requests.post(api_endpoint, headers=headers, json=report_data)
#     if response.status_code == 201:
#         st.success("Report successfully pushed to Salesforce.")
#     else:
#         st.error(f"Failed to push to Salesforce: {response.status_code} - {response.text}")

# def Getcallquality(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need call quality analysis for the given transcription.
#         The output should look like this:
#         Add-on Request by Customer: customer request...........
#         Action Taken for the request: action taken by ........
#         call rating: rating out of 10
#         Reason: reason for the rating
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']

# def Getinsights(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need insight summary from the given transcription.
#         The output should look like this:
#         Insights Summary: insight summary of the conversation.....
#         Sentiment: sentiment of the conversation.....
#         I need Insights Summary and Sentiment only.
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']

# def Separatespeakers(trans):
#     prompt = f"""
#     Below is a transcription of a conversation between two people, presented in paragraph form and not separated. Your task is to accurately separate the conversation into two distinct parts, one for each speaker, based on the order of speech. Label the speakers as **Person1** and **Person2** for the first and second speakers respectively, alternating based on the sequence. Do not assume specific roles (e.g., agent or customer); rely solely on the order of dialogue, natural flow, and contextual cues such as questions, responses, or pauses to determine speaker turns. Exclude the raw transcript or any extra labels from the output—provide only the separated dialogue with **Person1** and **Person2** labels.

#     Provide detailed examples to guide your separation:
#     - If a speaker initiates with a question or request (e.g., "Can you verify the items?"), assign it to Person1, and if the next part responds (e.g., "Of course, let me check..."), assign it to Person2.
#     - Use pauses (e.g., "(pause)") as indicators to confirm speaker switches where applicable.
#     - Ensure each speaker’s full dialogue is grouped together as a single turn before switching to the next speaker, starting Person2 on a new line after Person1’s complete turn. Do not split a speaker’s turn or include the raw transcript text.

#     The output should use bold text for speaker labels (**Person1**: ...) followed by their dialogue on the same line. Maintain the original wording, punctuation, and formatting (e.g., pauses in parentheses). Achieve 100% accuracy by carefully analyzing the dialogue flow, ensuring no speaker’s turn is misassigned or mixed with raw transcript text.

#     Transcription:
#     {trans}
#     """
#     body = {
#         "input": prompt,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 500,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.separate = response.json()['results'][0]['generated_text']

# def get_cos_files():
#     try:
#         all_files = []
#         continuation_token = None
#         while True:
#             params = {
#                 'Bucket': COS_BUCKET,
#                 'MaxKeys': 1000
#             }
#             if continuation_token:
#                 params['ContinuationToken'] = continuation_token
#             response = cos_client.list_objects_v2(**params)
#             contents = response.get('Contents', [])
#             files_with_metadata = [
#                 {'Key': obj['Key'], 'LastModified': obj['LastModified']}
#                 for obj in contents if obj['Key'].endswith('.json')
#             ]
#             all_files.extend(files_with_metadata)
#             if not response.get('IsTruncated'):
#                 break
#             continuation_token = response.get('NextContinuationToken')
#         if not all_files:
#             st.warning("No .json files found in the bucket 'ozonetell' after pagination. Please ensure JSON files are uploaded.")
#             return []
#         # Sort by LastModified to get the newest file
#         latest_file = max(all_files, key=lambda x: x['LastModified'])
#         return [latest_file['Key']]
#     except Exception as e:
#         st.error(f"Error fetching COS files: {e}")
#         return []

# def process_audio_from_cos(file_key):
#     try:
#         file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
#         json_data = json.loads(file_obj['Body'].read().decode('utf-8'))
        
#         # Debug: Display the raw JSON content
#         st.write("Raw JSON content for", file_key + ":", json.dumps(json_data, indent=2))
        
#         if 'AudioFile' not in json_data or not json_data['AudioFile']:
#             st.error(f"No valid 'AudioFile' URL found in {file_key}. Adding to failed files list for review.")
#             st.session_state.failed_files.append(file_key)
#             return

#         audio_url = json_data['AudioFile']
#         result = urllib.parse.urlparse(audio_url)
#         if not result.scheme:
#             st.error(f"Invalid URL '{audio_url}' in {file_key}: No scheme supplied. Perhaps you meant https://{audio_url}? Adding to failed files list for review.")
#             st.session_state.failed_files.append(file_key)
#             return

#         audio_response = requests.get(audio_url, stream=True)
#         if audio_response.status_code == 200:
#             audio_data = audio_response.content
#         else:
#             st.error(f"Failed to download audio from {audio_url} in {file_key}. Status code: {audio_response.status_code}")
#             st.session_state.failed_files.append(file_key)
#             return

#         url = "https://dev.assisto.tech/workflow_apis/process_file"
#         payload = {}
#         files = [('file', (file_key, io.BytesIO(audio_data), 'audio/mpeg'))]
#         headers = {}
        
#         response = requests.post(url, headers=headers, data=payload, files=files)
#         if response.status_code == 200:
#             transcript = response.json()['result'][0]['message']
#             st.session_state.raw_transcript = transcript
#             st.session_state.transcript = transcript
#             Getinsights(st.session_state.transcript)
#             Getcallquality(st.session_state.transcript)
#             Separatespeakers(st.session_state.transcript)
#             # Push to Salesforce after successful transcription
#             push_to_salesforce(st.session_state.raw_transcript, st.session_state.insights, st.session_state.callquality, st.session_state.separate)
#             st.session_state.last_processed_file = file_key
#         else:
#             st.error(f"Error from external API for {file_key}: {response.status_code} - {response.text}")
#             st.session_state.transcript = response.text
#     except Exception as e:
#         st.error(f"An error occurred while processing the file {file_key}: {e}")
#         st.session_state.transcript = str(e)

# # Layout
# with top1:
#     st.subheader("Select Audio from IBM COS")
#     json_files = get_cos_files()
#     if json_files:
#         selected_file = json_files[0]  # Automatically select the latest file
#         st.write(f"Automatically processing the latest file: {selected_file}")
#         if st.session_state.last_processed_file != selected_file:
#             process_audio_from_cos(selected_file)
#         else:
#             st.write("No new files to process. Last processed file:", st.session_state.last_processed_file)
#     else:
#         selected_file = st.selectbox("Choose an audio file", json_files, placeholder="No options to select.")
#         if st.button("Process Audio", type="primary", use_container_width=True) and selected_file:
#             process_audio_from_cos(selected_file)
#     # Display failed files if any
#     if st.session_state.failed_files:
#         st.warning(f"The following files failed due to invalid 'AudioFile' URLs: {st.session_state.failed_files}")
#         st.write("Please update these JSON files to include a valid 'AudioFile' key with a URL (e.g., https://example.com/audio.mp3).")

# with top2:
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     with st.container(height=300):
#         if st.session_state.transcript == "Select a JSON file to get transcript":
#             st.write("Transcript will appear here")
#         else:
#             st.subheader("Transcript")
#             st.write(st.session_state.raw_transcript)
#             st.write(st.session_state.separate)

# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)

#24/7 working
# import streamlit as st
# import requests
# import json
# import ibm_boto3
# from ibm_botocore.client import Config
# import io
# import urllib.parse
# from datetime import datetime
# import time

# # IBM COS Credentials
# COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
# COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
# COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
# COS_BUCKET = "ozonetell"

# # Initialize COS client
# cos_client = ibm_boto3.client(
#     's3',
#     ibm_api_key_id=COS_API_KEY,
#     ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
#     config=Config(signature_version='oauth'),
#     endpoint_url=COS_ENDPOINT
# )

# # Existing API credentials for Watsonx
# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"

# # Salesforce Credentials
# SALESFORCE_CLIENT_ID = "3MVG9wt4IL4O5wvKmuWykzw13DGFOnjtd2q0MhKTvjQRdylQtrxmuTnEq4i2_.s6sQSQ5YJMl.1n_ScCpSDSP"
# SALESFORCE_CLIENT_SECRET = "B7143F5B5BEA70B22F037608F6FDCD818AFEFDC88CD1588FB0608720471E9369"
# SALESFORCE_USERNAME = "impwatson@gadieltechnologies.com"
# SALESFORCE_PASSWORD = "Wave@#123456"
# SALESFORCE_TOKEN_URL = "https://login.salesforce.com/services/oauth2/token"
# SALESFORCE_INSTANCE_URL = "https://waveinfratech.my.salesforce.com"
# SALESFORCE_API_VERSION = "v58.0"

# # Session state initialization (unconditional)
# st.session_state.last_processed_file = st.session_state.get('last_processed_file', None)
# st.session_state.last_check_time = st.session_state.get('last_check_time', None)
# st.session_state.transcript = st.session_state.get('transcript', "Waiting for new JSON file...")
# st.session_state.insights = st.session_state.get('insights', "")
# st.session_state.callquality = st.session_state.get('callquality', "")
# st.session_state.separate = st.session_state.get('separate', "")
# st.session_state.raw_transcript = st.session_state.get('raw_transcript', "Raw transcript will appear here...")
# st.session_state.failed_files = st.session_state.get('failed_files', [])

# # Page config
# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights (24/7 Mode)")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights (24/7 Mode)</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0e1117;
#     }
#     .css-1d8v1u7, .css-1a32f9v {
#         color: #ffffff !important;
#         font-size: 16px !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
#     data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
#     response = requests.post(auth_url, headers=headers, data=data)
#     return response.json()['access_token']

# def get_salesforce_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}
#     data = {
#         "grant_type": "password",
#         "client_id": SALESFORCE_CLIENT_ID,
#         "client_secret": SALESFORCE_CLIENT_SECRET,
#         "username": SALESFORCE_USERNAME,
#         "password": SALESFORCE_PASSWORD
#     }
#     response = requests.post(SALESFORCE_TOKEN_URL, headers=headers, data=data)
#     if response.status_code == 200:
#         return response.json()['access_token']
#     else:
#         st.error(f"Failed to get Salesforce token: {response.text}")
#         return None

# def push_to_salesforce(transcript, insights, callquality, separate):
#     access_token = get_salesforce_token()
#     if not access_token:
#         return

#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     report_data = {
#         "Transcript__c": transcript,
#         "Insights__c": insights,
#         "CallQuality__c": callquality,
#         "SeparatedSpeakers__c": separate
#     }
#     api_endpoint = f"{SALESFORCE_INSTANCE_URL}/services/data/{SALESFORCE_API_VERSION}/sobjects/Call_Report__c/"
#     response = requests.post(api_endpoint, headers=headers, json=report_data)
#     if response.status_code == 201:
#         st.success("Report successfully pushed to Salesforce.")
#     else:
#         st.error(f"Failed to push to Salesforce: {response.status_code} - {response.text}")

# def Getcallquality(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need call quality analysis for the given transcription.
#         The output should look like this:
#         Add-on Request by Customer: customer request...........
#         Action Taken for the request: action taken by ........
#         call rating: rating out of 10
#         Reason: reason for the rating
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']

# def Getinsights(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need insight summary from the given transcription.
#         The output should look like this:
#         Insights Summary: insight summary of the conversation.....
#         Sentiment: sentiment of the conversation.....
#         I need Insights Summary and Sentiment only.
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']

# def Separatespeakers(trans):
#     prompt = f"""
#     Below is a transcription of a conversation between two people, presented in paragraph form and not separated. Your task is to accurately separate the conversation into two distinct parts, one for each speaker, based on the order of speech. Label the speakers as **Person1** and **Person2** for the first and second speakers respectively, alternating based on the sequence. Do not assume specific roles (e.g., agent or customer); rely solely on the order of dialogue, natural flow, and contextual cues such as questions, responses, or pauses to determine speaker turns. Exclude the raw transcript or any extra labels from the output—provide only the separated dialogue with **Person1** and **Person2** labels.

#     Provide detailed examples to guide your separation:
#     - If a speaker initiates with a question or request (e.g., "Can you verify the items?"), assign it to Person1, and if the next part responds (e.g., "Of course, let me check..."), assign it to Person2.
#     - Use pauses (e.g., "(pause)") as indicators to confirm speaker switches where applicable.
#     - Ensure each speaker’s full dialogue is grouped together as a single turn before switching to the next speaker, starting Person2 on a new line after Person1’s complete turn. Do not split a speaker’s turn or include the raw transcript text.

#     The output should use bold text for speaker labels (**Person1**: ...) followed by their dialogue on the same line. Maintain the original wording, punctuation, and formatting (e.g., pauses in parentheses). Achieve 100% accuracy by carefully analyzing the dialogue flow, ensuring no speaker’s turn is misassigned or mixed with raw transcript text.

#     Transcription:
#     {trans}
#     """
#     body = {
#         "input": prompt,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 500,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.separate = response.json()['results'][0]['generated_text']

# def get_cos_files():
#     try:
#         all_files = []
#         continuation_token = None
#         while True:
#             params = {
#                 'Bucket': COS_BUCKET,
#                 'MaxKeys': 1000
#             }
#             if continuation_token:
#                 params['ContinuationToken'] = continuation_token
#             response = cos_client.list_objects_v2(**params)
#             contents = response.get('Contents', [])
#             files_with_metadata = [
#                 {'Key': obj['Key'], 'LastModified': obj['LastModified']}
#                 for obj in contents if obj['Key'].endswith('.json')
#             ]
#             all_files.extend(files_with_metadata)
#             if not response.get('IsTruncated'):
#                 break
#             continuation_token = response.get('NextContinuationToken')
#         if not all_files:
#             st.warning("No .json files found in the bucket 'ozonetell' after pagination.")
#             return None
#         # Sort by LastModified to get the newest file
#         latest_file = max(all_files, key=lambda x: x['LastModified'])
#         return latest_file
#     except Exception as e:
#         st.error(f"Error fetching COS files: {e}")
#         return None

# def process_audio_from_cos(file_key):
#     try:
#         file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
#         json_data = json.loads(file_obj['Body'].read().decode('utf-8'))
        
#         st.write("Raw JSON content for", file_key + ":", json.dumps(json_data, indent=2))
        
#         if 'AudioFile' not in json_data or not json_data['AudioFile']:
#             st.error(f"No valid 'AudioFile' URL found in {file_key}. Adding to failed files list.")
#             st.session_state.failed_files.append(file_key)
#             return

#         audio_url = json_data['AudioFile']
#         result = urllib.parse.urlparse(audio_url)
#         if not result.scheme:
#             st.error(f"Invalid URL '{audio_url}' in {file_key}. Adding to failed files list.")
#             st.session_state.failed_files.append(file_key)
#             return

#         audio_response = requests.get(audio_url, stream=True)
#         if audio_response.status_code == 200:
#             audio_data = audio_response.content
#         else:
#             st.error(f"Failed to download audio from {audio_url}. Status code: {audio_response.status_code}")
#             st.session_state.failed_files.append(file_key)
#             return

#         url = "https://dev.assisto.tech/workflow_apis/process_file"
#         payload = {}
#         files = [('file', (file_key, io.BytesIO(audio_data), 'audio/mpeg'))]
#         headers = {}
        
#         response = requests.post(url, headers=headers, data=payload, files=files)
#         if response.status_code == 200:
#             transcript = response.json()['result'][0]['message']
#             st.session_state.raw_transcript = transcript
#             st.session_state.transcript = transcript
#             Getinsights(st.session_state.transcript)
#             Getcallquality(st.session_state.transcript)
#             Separatespeakers(st.session_state.transcript)
#             push_to_salesforce(st.session_state.raw_transcript, st.session_state.insights, st.session_state.callquality, st.session_state.separate)
#             st.session_state.last_processed_file = file_key
#             st.session_state.last_check_time = datetime.now()
#         else:
#             st.error(f"Error from external API for {file_key}: {response.status_code} - {response.text}")
#     except Exception as e:
#         st.error(f"Error processing {file_key}: {e}")
#         st.session_state.failed_files.append(file_key)

# # Main 24/7 loop
# def run_24_7():
#     while True:
#         latest_file = get_cos_files()
#         if latest_file and latest_file['Key'] != st.session_state.last_processed_file:
#             st.write(f"New file detected: {latest_file['Key']} (Last Modified: {latest_file['LastModified']})")
#             process_audio_from_cos(latest_file['Key'])
#         else:
#             if st.session_state.last_processed_file:
#                 st.write(f"No new files. Last processed: {st.session_state.last_processed_file} at {st.session_state.last_check_time}")
#             else:
#                 st.write("Waiting for new JSON files...")
#         time.sleep(60)  # Check every 60 seconds (adjust as needed)

# # Layout
# with top1:
#     st.subheader("24/7 Audio Processing from IBM COS")
#     if st.button("Start 24/7 Processing", type="primary", use_container_width=True):
#         run_24_7()
#     # Display status
#     st.write(f"Last processed file: {st.session_state.last_processed_file or 'None'}")
#     st.write(f"Last check time: {st.session_state.last_check_time or 'Never'}")
#     # Display failed files if any
#     if st.session_state.failed_files:
#         st.warning(f"The following files failed: {st.session_state.failed_files}")
#         st.write("Please update these JSON files with valid 'AudioFile' URLs.")

# with top2:
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     with st.container(height=300):
#         st.subheader("Transcript")
#         st.write(st.session_state.raw_transcript)
#         st.write(st.session_state.separate)

# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)

# # Start the 24/7 process in a separate thread or background task in production
# if __name__ == "__main__":
#     run_24_7()

#24/7 working
# import streamlit as st
# import requests
# import json
# import ibm_boto3
# from ibm_botocore.client import Config
# import io
# import urllib.parse
# from datetime import datetime
# import time
# import base64

# # IBM COS Credentials
# COS_API_KEY = "2PjLRmZ3Ay-WQpuE33qGaQzDohwVJIzocHlABKayUsNV"
# COS_SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/fddc2a92db904306b413ed706665c2ff:e99c3906-0103-4257-bcba-e455e7ced9b7::"
# COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
# COS_BUCKET = "ozonetell"

# # Initialize COS client
# cos_client = ibm_boto3.client(
#     's3',
#     ibm_api_key_id=COS_API_KEY,
#     ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
#     config=Config(signature_version='oauth'),
#     endpoint_url=COS_ENDPOINT
# )

# # Existing API credentials for Watsonx
# api_key = "3Vj-0udUsnRjiJwBKNGAEcHNpiS-xi6VX-5tU2VZWHij"
# url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
# project_id = "4152f31e-6a49-40aa-9b62-0ecf629aae42"
# model_id = "meta-llama/llama-3-2-90b-vision-instruct"
# auth_url = "https://iam.cloud.ibm.com/identity/token"

# # Salesforce Credentials
# SALESFORCE_CLIENT_ID = "3MVG9wt4IL4O5wvKmuWykzw13DGFOnjtd2q0MhKTvjQRdylQtrxmuTnEq4i2_.s6sQSQ5YJMl.1n_ScCpSDSP"
# SALESFORCE_CLIENT_SECRET = "B7143F5B5BEA70B22F037608F6FDCD818AFEFDC88CD1588FB0608720471E9369"
# SALESFORCE_USERNAME = "impwatson@gadieltechnologies.com"
# SALESFORCE_PASSWORD = "Wave@#123456"
# SALESFORCE_TOKEN_URL = "https://login.salesforce.com/services/oauth2/token"
# SALESFORCE_INSTANCE_URL = "https://waveinfratech.my.salesforce.com"
# SALESFORCE_API_VERSION = "v58.0"

# # Session state initialization (unconditional)
# st.session_state.last_processed_file = st.session_state.get('last_processed_file', None)
# st.session_state.last_check_time = st.session_state.get('last_check_time', None)
# st.session_state.transcript = st.session_state.get('transcript', "Waiting for new JSON file...")
# st.session_state.insights = st.session_state.get('insights', "")
# st.session_state.callquality = st.session_state.get('callquality', "")
# st.session_state.separate = st.session_state.get('separate', "")
# st.session_state.raw_transcript = st.session_state.get('raw_transcript', "Raw transcript will appear here...")
# st.session_state.failed_files = st.session_state.get('failed_files', [])

# # Page config
# st.set_page_config(layout="wide", page_title="Wave Infra Call Insights (24/7 Mode)")
# st.markdown("<h1 style='text-align:center'>Wave Infra Call Insights (24/7 Mode)</h1>", unsafe_allow_html=True)
# st.markdown("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'>", unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0e1117;
#     }
#     .css-1d8v1u7, .css-1a32f9v {
#         color: #ffffff !important;
#         font-size: 16px !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# top1, top2 = st.columns(2)
# bottom1, bottom2 = st.columns(2)

# def access_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
#     data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
#     response = requests.post(auth_url, headers=headers, data=data)
#     return response.json()['access_token']

# def get_salesforce_token():
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}
#     data = {
#         "grant_type": "password",
#         "client_id": SALESFORCE_CLIENT_ID,
#         "client_secret": SALESFORCE_CLIENT_SECRET,
#         "username": SALESFORCE_USERNAME,
#         "password": SALESFORCE_PASSWORD
#     }
#     response = requests.post(SALESFORCE_TOKEN_URL, headers=headers, data=data)
#     if response.status_code == 200:
#         return response.json()['access_token']
#     else:
#         st.error(f"Failed to get Salesforce token: {response.status_code} - {response.text}")
#         return None

# def push_to_salesforce(transcript, insights, callquality, separate):
#     access_token = get_salesforce_token()
#     if not access_token:
#         return

#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     # Try custom object first
#     custom_object_data = {
#         "Transcript__c": transcript,
#         "Insights__c": insights,
#         "CallQuality__c": callquality,
#         "SeparatedSpeakers__c": separate
#     }
#     custom_endpoint = f"{SALESFORCE_INSTANCE_URL}/services/data/{SALESFORCE_API_VERSION}/sobjects/Call_Report__c/"
#     response = requests.post(custom_endpoint, headers=headers, json=custom_object_data)
#     if response.status_code == 201:
#         st.success("Report successfully pushed to Call_Report__c.")
#         return
#     else:
#         st.error(f"Failed to push to Call_Report__c: {response.status_code} - {response.text}")

#     # Fallback to ContentNote (modern note type)
#     content_note_data = {
#         "Title": f"Call Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
#         "Content": base64.b64encode(f"Transcript: {transcript}\nInsights: {insights}\nCall Quality: {callquality}\nSeparated Speakers: {separate}".encode()).decode(),
#         "SharingOption": "A"  # A = All Users can view
#     }
#     content_note_endpoint = f"{SALESFORCE_INSTANCE_URL}/services/data/{SALESFORCE_API_VERSION}/sobjects/ContentNote/"
#     response = requests.post(content_note_endpoint, headers=headers, json=content_note_data)
#     if response.status_code == 201:
#         st.success("Report successfully pushed to ContentNote as fallback.")
#     else:
#         st.error(f"Failed to push to ContentNote: {response.status_code} - {response.text}")

# def Getcallquality(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need call quality analysis for the given transcription.
#         The output should look like this:
#         Add-on Request by Customer: customer request...........
#         Action Taken for the request: action taken by ........
#         call rating: rating out of 10
#         Reason: reason for the rating
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.callquality = response.json()['results'][0]['generated_text']

# def Getinsights(trans):
#     body = {
#         "input": f"""
#         Below is a transcription of a conversation between two people. Need insight summary from the given transcription.
#         The output should look like this:
#         Insights Summary: insight summary of the conversation.....
#         Sentiment: sentiment of the conversation.....
#         I need Insights Summary and Sentiment only.
#         Transcription:
#         {trans}
#         """,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 300,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.insights = response.json()['results'][0]['generated_text']

# def Separatespeakers(trans):
#     prompt = f"""
#     Below is a transcription of a conversation between two people, presented in paragraph form and not separated. Your task is to accurately separate the conversation into two distinct parts, one for each speaker, based on the order of speech. Label the speakers as **Person1** and **Person2** for the first and second speakers respectively, alternating based on the sequence. Do not assume specific roles (e.g., agent or customer); rely solely on the order of dialogue, natural flow, and contextual cues such as questions, responses, or pauses to determine speaker turns. Exclude the raw transcript or any extra labels from the output—provide only the separated dialogue with **Person1** and **Person2** labels.

#     Provide detailed examples to guide your separation:
#     - If a speaker initiates with a question or request (e.g., "Can you verify the items?"), assign it to Person1, and if the next part responds (e.g., "Of course, let me check..."), assign it to Person2.
#     - Use pauses (e.g., "(pause)") as indicators to confirm speaker switches where applicable.
#     - Ensure each speaker’s full dialogue is grouped together as a single turn before switching to the next speaker, starting Person2 on a new line after Person1’s complete turn. Do not split a speaker’s turn or include the raw transcript text.

#     The output should use bold text for speaker labels (**Person1**: ...) followed by their dialogue on the same line. Maintain the original wording, punctuation, and formatting (e.g., pauses in parentheses). Achieve 100% accuracy by carefully analyzing the dialogue flow, ensuring no speaker’s turn is misassigned or mixed with raw transcript text.

#     Transcription:
#     {trans}
#     """
#     body = {
#         "input": prompt,
#         "parameters": {
#             "decoding_method": "greedy",
#             "max_new_tokens": 500,
#             "min_new_tokens": 30,
#             "stop_sequences": [";"],
#             "repetition_penalty": 1.05,
#             "temperature": 0.5
#         },
#         "model_id": model_id,
#         "project_id": project_id
#     }
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {access_token()}"
#     }
#     response = requests.post(url, headers=headers, json=body)
#     st.session_state.separate = response.json()['results'][0]['generated_text']

# def get_cos_files():
#     try:
#         all_files = []
#         continuation_token = None
#         while True:
#             params = {
#                 'Bucket': COS_BUCKET,
#                 'MaxKeys': 1000
#             }
#             if continuation_token:
#                 params['ContinuationToken'] = continuation_token
#             response = cos_client.list_objects_v2(**params)
#             contents = response.get('Contents', [])
#             files_with_metadata = [
#                 {'Key': obj['Key'], 'LastModified': obj['LastModified']}
#                 for obj in contents if obj['Key'].endswith('.json') and not obj['Key'].startswith('failed/')
#             ]
#             all_files.extend(files_with_metadata)
#             if not response.get('IsTruncated'):
#                 break
#             continuation_token = response.get('NextContinuationToken')
#         if not all_files:
#             st.warning("No .json files found in the bucket 'ozonetell' after pagination (excluding failed files).")
#             return None
#         # Sort by LastModified to get the newest file
#         return max(all_files, key=lambda x: x['LastModified'])
#     except Exception as e:
#         st.error(f"Error fetching COS files: {e}")
#         return None

# def move_file_to_failed(file_key):
#     try:
#         new_key = f"failed/{file_key}"
#         cos_client.copy_object(Bucket=COS_BUCKET, CopySource={'Bucket': COS_BUCKET, 'Key': file_key}, Key=new_key)
#         cos_client.delete_object(Bucket=COS_BUCKET, Key=file_key)
#         st.write(f"Moved {file_key} to failed/{file_key} due to processing issue.")
#     except Exception as e:
#         st.error(f"Error moving {file_key} to failed: {e}")

# def process_audio_from_cos(file_key):
#     try:
#         file_obj = cos_client.get_object(Bucket=COS_BUCKET, Key=file_key)
#         json_data = json.loads(file_obj['Body'].read().decode('utf-8'))
        
#         st.write("Raw JSON content for", file_key + ":", json.dumps(json_data, indent=2))
        
#         if 'AudioFile' not in json_data or not json_data['AudioFile']:
#             st.error(f"No valid 'AudioFile' URL found in {file_key}.")
#             move_file_to_failed(file_key)
#             st.session_state.failed_files.append(file_key)
#             return False

#         audio_url = json_data['AudioFile']
#         result = urllib.parse.urlparse(audio_url)
#         if not result.scheme:
#             st.error(f"Invalid URL '{audio_url}' in {file_key}.")
#             move_file_to_failed(file_key)
#             st.session_state.failed_files.append(file_key)
#             return False

#         audio_response = requests.get(audio_url, stream=True)
#         if audio_response.status_code == 200:
#             audio_data = audio_response.content
#         else:
#             st.error(f"Failed to download audio from {audio_url}. Status code: {audio_response.status_code}")
#             move_file_to_failed(file_key)
#             st.session_state.failed_files.append(file_key)
#             return False

#         url = "https://dev.assisto.tech/workflow_apis/process_file"
#         payload = {}
#         files = [('file', (file_key, io.BytesIO(audio_data), 'audio/mpeg'))]
#         headers = {}
        
#         max_retries = 3
#         for attempt in range(max_retries):
#             response = requests.post(url, headers=headers, data=payload, files=files)
#             if response.status_code == 200:
#                 try:
#                     result = response.json()
#                     if result.get('result') and len(result['result']) > 0 and 'message' in result['result'][0]:
#                         transcript = result['result'][0]['message']
#                         st.session_state.raw_transcript = transcript
#                         st.session_state.transcript = transcript
#                         Getinsights(st.session_state.transcript)
#                         Getcallquality(st.session_state.transcript)
#                         Separatespeakers(st.session_state.transcript)
#                         push_to_salesforce(st.session_state.raw_transcript, st.session_state.insights, st.session_state.callquality, st.session_state.separate)
#                         st.session_state.last_processed_file = file_key
#                         st.session_state.last_check_time = datetime.now()
#                         return True
#                     else:
#                         st.error(f"Unexpected API response structure for {file_key}: {result}")
#                         move_file_to_failed(file_key)
#                         st.session_state.failed_files.append(file_key)
#                         return False
#                 except json.JSONDecodeError:
#                     st.error(f"Failed to decode API response for {file_key}")
#                     if attempt < max_retries - 1:
#                         time.sleep(2 ** attempt)  # Exponential backoff
#                         continue
#                     move_file_to_failed(file_key)
#                     st.session_state.failed_files.append(file_key)
#                     return False
#             else:
#                 st.error(f"API call failed for {file_key} (Status: {response.status_code})")
#                 if attempt < max_retries - 1:
#                     time.sleep(2 ** attempt)  # Exponential backoff
#                     continue
#                 move_file_to_failed(file_key)
#                 st.session_state.failed_files.append(file_key)
#                 return False
#         return False
#     except Exception as e:
#         st.error(f"Error processing {file_key}: {e}")
#         st.session_state.failed_files.append(file_key)
#         return False

# # Main 24/7 loop
# def run_24_7():
#     while True:
#         latest_file = get_cos_files()
#         if latest_file:
#             file_key = latest_file['Key']
#             if file_key != st.session_state.last_processed_file:
#                 st.write(f"New file detected: {file_key} (Last Modified: {latest_file['LastModified']})")
#                 success = process_audio_from_cos(file_key)
#                 if not success:
#                     # Move to failed and try the next file
#                     continue
#             else:
#                 st.write(f"No new files. Last processed: {st.session_state.last_processed_file} at {st.session_state.last_check_time}")
#         else:
#             st.write("Waiting for new JSON files...")
#         time.sleep(60)  # Check every 60 seconds (adjust as needed)

# # Layout
# with top1:
#     st.subheader("24/7 Audio Processing from IBM COS")
#     if st.button("Start 24/7 Processing", type="primary", use_container_width=True):
#         run_24_7()
#     # Display status
#     st.write(f"Last processed file: {st.session_state.last_processed_file or 'None'}")
#     st.write(f"Last check time: {st.session_state.last_check_time or 'Never'}")
#     # Display failed files if any
#     if st.session_state.failed_files:
#         st.warning(f"The following files failed: {st.session_state.failed_files}")
#         st.write("These files have been moved to the 'failed/' prefix. Update them with valid 'AudioFile' URLs and move back to the root if needed.")

# with top2:
#     st.subheader("Call Transcript using Watsonx Speech-To-text")
#     with st.container(height=300):
#         st.subheader("Transcript")
#         st.write(st.session_state.raw_transcript)
#         st.write(st.session_state.separate)

# with bottom1:
#     st.subheader("Call Insights by watsonx.ai")
#     with st.container(height=300, key=2):
#         st.write(st.session_state.insights)

# with bottom2:
#     st.subheader("Call quality analysis by watsonx.ai")
#     with st.container(height=300, key=3):
#         st.write(st.session_state.callquality)

# # Start the 24/7 process in a separate thread or background task in production
# if __name__ == "__main__":
#     run_24_7()