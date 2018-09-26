#https://googlecloudplatform.github.io/google-cloud-python/latest/speech/index.html
#https://cloud.google.com/speech-to-text/docs/basics

def legenda_gcs(gcs_uri):
	from google.cloud import speech_v1
	from google.cloud.speech_v1 import enums
	#import os
	#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/path/to/file.json"
	
	client = speech_v1.SpeechClient()

	encoding = enums.RecognitionConfig.AudioEncoding.FLAC
	sample_rate_hertz = 44100
	language_code = 'pt-BR'
	config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
	#uri = 'gs://legenda/mono02.flac'
	audio = {'uri': gcs_uri}

	operation = client.long_running_recognize(config, audio)
	print('Esperando a conclusao da operacao API...')
	response = client.recognize(config, audio)
	
	file = open('c:\legenda_api.txt','w')
	for result in response.results:
		file.write('{}\n'.format(result.alternatives[0].transcript))
		
	file.close()
	
def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
	
	
	
	
	#for result in response.results:
	#    file.write('{}\n'.format(result.alternatives[0].transcript))
    #file.close()

