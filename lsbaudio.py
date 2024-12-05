import wave

def hide_audio_message(input_audio, output_audio, message):
    audio = wave.open(input_audio, 'rb')
    frames = bytearray(list(audio.readframes(audio.getnframes())))
    audio.close()
    
    message_binary = ''.join(format(ord(char), '08b') for char in message) + '11111111'
    for i in range(len(message_binary)):
        frames[i] = (frames[i] & ~1) | int(message_binary[i])

    new_audio = wave.open(output_audio, 'wb')
    new_audio.setparams(audio.getparams())
    new_audio.writeframes(frames)
    new_audio.close()
    print("Message hidden successfully!")

# Usage
hide_audio_message('input.wav', 'output.wav', 'HELLO')
