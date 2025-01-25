import json

def loadVideos():
    try:
        with open("practice.txt", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def saveVideo(video):
    with open("practice.txt", 'w') as file:
        json.dump(video, file)

def List_All_Videos(videos):
    print("\n")
    print("-"*40)
    for index, vid in enumerate(videos, start=1):
        print(f"{index}. {vid['Name']}, Duration {vid['Duration']}")
    print("-"*40)

def Add_Videos(videos):
    name = input("Enter name of video : ")
    duration = input("Enter Duration of video : ")
    videos.append({"Name":name, "Duration":duration})
    saveVideo(videos)

def update_Videos(videos):
    List_All_Videos(videos)
    update = int(input("Enter Video number to update : "))
    if 1<= update <= len(videos):
        name = input("Enter name of video : ")
        duration = input("Enter Duration of video : ")
        videos[update-1] = {'Name':name, 'Duration':duration}
        saveVideo(videos)
    else:
        print("Enter value choice to update video")

def Delete_Videos(videos):
    List_All_Videos(videos)
    index = int(input("Enter video number you want to Delete : "))
    if 1<= index <= len(videos):
        del videos[index-1]
        saveVideo(videos)
    else:
        print("Enter a Valid number to Delete video")

def main():
    videos = loadVideos()
    while True:
        print("Choose A List")
        print("1: List All Videos")
        print("2: Add Video")
        print("3: Update Video")
        print("4: Delete Video")
        print("5: Exit")

        choice = input("Enter your choice : ")

        match choice:
            case '1':
                List_All_Videos(videos)
            case '2':
                Add_Videos(videos)
            case '3':
                update_Videos(videos)
            case '4':
                Delete_Videos(videos)
            case '5':
                break
            case __:
                print("Enter Valid Choice")
        
if __name__ == "__main__":
    main()