import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

def add_video(videos):
    name=input("Enter the name")
    time=input("Enter the time")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name= input("Enter the new video name")
        time= input("Enter the new video time")
        videos[index-1]= {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selection")

def delete_video(videos):
    pass


def main():   
    while True:
        videos= load_data()
        print("YOUTUBE MANAGER APP | Choose an option ")
        print("1. List all Youtube Videos ")
        print("2. Add a Youtube Video ")
        print("3. Update a Youtube Video details ")
        print("4. Delete a Youtube Video ")
        print("Exit the app")
        choice= input("Enter your choice")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video('videos')
            case '4':
                delete_video('videos')
            case '5':
                break
            case __:
                print("Invalid Choice")

if __name__ == "__main__":
    main()

 
    

