# Route -> api_generate
def gen_api(list, filesuffix):

  # Create file paths to the actual files in storage for use in Transcode function
  def create_file_paths(file_names):
    base_path = "downsamp/" # this needs to be dynamic
    file_paths = []
  
    for index, file_name in enumerate(file_names, start=1):
        # Extract the body part (e.g., TORSO, LEFTARM)
        body_part = file_name.split('_')[0]
        final_body_part = body_part.split('-')[0]
  
        # Create the subdirectory based on the index and body part
        subdirectory = f"{index}_{final_body_part}/"
  
        # Create the full file path
        file_path = base_path + subdirectory + file_name
  
        file_paths.append(file_path)
  
    return file_paths

  result_paths = create_file_paths(list)

  # Create last layer ie.REARTORSO and add it to the paths
  substrings = result_paths[0].split('/')
  
  third_substring = substrings[2] # Torso file name

  torso_chosen = third_substring.split('.')[0] # Removal of .mov extension
  
  substrings_7 = result_paths[6].split('/') 
  
  new_reartorso = substrings_7[0] + "/8_REARTORSO/REAR" + torso_chosen[:-1] + "8.mov"
  
  result_paths.append(new_reartorso)
  result_paths.append("PresBG_WHITE_SmokeBackplate_v03_1k.mov")
  
  result_paths.reverse()
  print(result_paths)
  
  final_url = TranscodeOptApi(result_paths, f'{filesuffix}.mp4')
  return final_url


# Generate from specific category(Elemental, Zoological, etc.)
def gen_func_QA3(filesuffix):
  print(f"File suffix = {filesuffix}")
  directory = "downsamp"
  folder_dict = {}
  unique_name = "_Bot"

  # Get the list of items (file or folder) in the given directory
  items = sorted(os.listdir(directory),
                 key=lambda x: (re.sub('[^0-9a-zA-Z]+', '', x.lower()), x))

  # Iterate through each item (file or folder) in the sorted list
  for item in items:
    item_path = os.path.join(directory, item)

    # Check if it's a directory
    if os.path.isdir(item_path):
      # Get the list of files in the directory with their full paths
      files_in_folder = [
          os.path.join(item_path, f) for f in os.listdir(item_path)
          if os.path.isfile(os.path.join(item_path, f)) and unique_name in f
      ]
      folder_dict[item] = files_in_folder

  result_dict = folder_dict

  random_list = [random.choice(files) for files in result_dict.values()]
  #random_list.append("PresBG_WHITE_SmokeBackplate_v03_1k.mov")
  random_list.append("SmokeBG_1080p.mp4")

  substrings = random_list[0].split('/')

  # Extract the 3rd substring (index 2, since indexing starts from 0)
  third_substring = substrings[2]
  torso_chosen = third_substring.split('.')[0]

  substrings_7 = random_list[7].split('/')

  new_reartorso = substrings_7[0] + "/" + substrings_7[
      1] + "/REAR" + torso_chosen[:-1] + "8.mov"

  random_list[7] = new_reartorso

  random_list.reverse()

  TranscodeOpt(random_list, f'{filesuffix}.mp4')



# Random generation, store in wasabi and return url to user
def gen_func(filesuffix):

  def create_folder_dictionary(directory):
    folder_dict = {}

    # Get the list of items (file or folder) in the given directory
    items = sorted(os.listdir(directory),
                   key=lambda x: (re.sub('[^0-9a-zA-Z]+', '', x.lower()), x))

    # Iterate through each item (file or folder) in the sorted list
    for item in items:
      item_path = os.path.join(directory, item)

      # Check if it's a directory
      if os.path.isdir(item_path):
        # Get the list of files in the directory with their full paths
        files_in_folder = [
            os.path.join(item_path, f) for f in os.listdir(item_path)
            if os.path.isfile(os.path.join(item_path, f))
        ]
        folder_dict[item] = files_in_folder

    return folder_dict

  # Replace 'your_directory_path' with the actual directory path
  directory_path = 'downsamp'

  # Create the folder dictionary
  result_dict = create_folder_dictionary(directory_path)

  # Randomly select an item from each array and store in random_list
  random_list = [random.choice(files) for files in result_dict.values()]
  random_list.append("PresBG_WHITE_SmokeBackplate_v03_1k.mov")

  substrings = random_list[0].split('/')

  # Extract the 3rd substring (index 2, since indexing starts from 0)
  third_substring = substrings[2]
  torso_chosen = third_substring.split('.')[0]

  substrings_7 = random_list[7].split('/')

  new_reartorso = substrings_7[0] + "/" + substrings_7[
      1] + "/REAR" + torso_chosen[:-1] + "8.mov"
  print(new_reartorso)

  random_list[7] = new_reartorso

  random_list.reverse()

  final_url = TranscodeOptApi(random_list, f'{filesuffix}.mp4')
  return final_url