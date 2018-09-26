def legenda_gcs(gcs_uri):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='pt-BR')
		

    operation = client.long_running_recognize(config, audio)

    print('Esperando a conclusao da operacao...')
    response = operation.result(timeout=3000)
    file = open('c:\legenda2.txt','w')
    
    for result in response.results:
     	#print(u'Legenda: {}'.format(result.alternatives[0].transcript))
    	#print('Acuracia: {}'.format(result.alternatives[0].confidence))
        file.write('{}\n'.format(result.alternatives[0].transcript))
    
    file.close()
	
	
#ffmpeg.exe -i "flac1.flac" -ac 1 mono1.flac

	
#gsutil acl ch -u AllUsers:R "gs://legenda/mono02.flac" para deixar arquivo publico no Storage
#set GOOGLE_APPLICATION_CREDENTIALS = c:\MyProject.json

##Ambiente de desenvolvimento do Python##
#cd your-project
#virtualenv --python python3 env
#.\env\Scripts\activate