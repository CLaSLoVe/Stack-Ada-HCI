import socket
import time
import threading
import atexit

def send_eye_data(eye_socket):
    while True:
        eye_data = b'eye tracking data'
        eye_socket.sendto(eye_data, ('localhost', 8001))
        time.sleep(0.1)

def send_scene_data(scene_socket):
    while True:
        scene_data = b'scene parameter data'
        scene_socket.sendto(scene_data, ('localhost', 8002))
        time.sleep(0.5)


def close_socket():
    print("Closing socket connection...")
    client_socket.close()


if __name__ == '__main__':
    print("Creating socket client...")
    # create a socket client for sending data
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Creating threads to send data...")
    # create two threads to send data
    eye_thread = threading.Thread(target=send_eye_data, args=(client_socket,))
    scene_thread = threading.Thread(target=send_scene_data, args=(client_socket,))
    eye_thread.start()
    scene_thread.start()

    # register exit handler to close socket connection
    atexit.register(close_socket)

    print("Waiting for threads to finish...")
    # wait for threads to finish
    eye_thread.join()
    scene_thread.join()
    print("All threads finished.")