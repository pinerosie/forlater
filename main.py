  while location:
        location = input("Enter a location (city name or latitude,longitude): ").strip()
        if location:
            try:
                weather_data = current_weather(location)
                for forecast in weather_data:
                    pprint(forecast)
            except ValueError as e:
                print(repr(e))
                location = ""


    for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
        if index >= max_images:
            return index
        original_size_img_not_fixed = bytes(fixed_full_res_image, "ascii").decode(
            "unicode-escape"
        )
        original_size_img = bytes(original_size_img_not_fixed, "ascii").decode(
            "unicode-escape"
        )
        opener = urllib.request.build_opener()
        opener.addheaders = [
            (
       if not os.path.exists(path_name):
            os.makedirs(path_name)
        urllib.request.urlretrieve(  # noqa: S310
            original_size_img, f"{path_name}/original_size_img_{index}.jpg"
        )
    return index
