def print_object(data) :
    name = data['name']
    alias = data['alias']
    social_count = data['social_count']

    print(f" name: {name}, alias: {alias}, social {social_count}")

def compare_object(object_a, object_b):
    social_count_a = object_a['social_count']
    social_count_b = object_b['social_count']

    if social_count_a > social_count_b:
        return 'a'
    elif social_count_a < social_count_b:
        return 'b'