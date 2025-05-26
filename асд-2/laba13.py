#Решить задачу о раскладке по ящикам

def pack_boxes(items, volume):
    items.sort(reverse=True)

    boxes = []

    for item in items:
        found_box = False

        for box in boxes:
            if sum(box) + item <= volume:
                box.append(item)
                found_box = True
                break

        if not found_box:
            boxes.append([item])

    return boxes

items = [4, 5, 2, 7, 3, 6]
volume = 10

pack_boxes(items, volume)
