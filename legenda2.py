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
    file = open('c:\legenda.txt','w')
    for result in response.results:
        #print(u'Legenda: {}'.format(result.alternatives[0].transcript))
        #print('Acuracia: {}'.format(result.alternatives[0].confidence))
        file.write('{}\n'.format(result.alternatives[0].transcript))
    file.close()
	
