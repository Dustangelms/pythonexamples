import googleapiclient.discovery


# Google clients

def create_google_spreadsheets_client_with_adc():
    return googleapiclient.discovery.build('sheets', 'v4')


def get_google_spreadsheets_object_info(
    client,
    object_id
):
    request = client.spreadsheets().get(
        spreadsheetId =
            object_id
    )
    response = request.execute()
    return\
        response.get('properties'),\
        response.get('sheets')


def read_region_from_google_spreadsheets_object(
    client,
    object_id,
    range_a1
):
    request = client.spreadsheets().values().get(
        spreadsheetId =
            object_id,
        range =
            range_a1
    )
    response = request.execute()
    return response.get('values')


def read_regions_from_google_spreadsheets_object(
    client,
    object_id,
    ranges_a1
):
    request = client.spreadsheets().values().batchGet(
        spreadsheetId =
            object_id,
        ranges =
            ranges_a1
    )
    response = request.execute()
    return\
        list(
            map(
                lambda region_data:
                    region_data.get('values'),
                response.get('valueRanges')
            )
        )


def write_region_to_google_spreadsheets_object(
    client,
    object_id,
    range_a1,
    region
):
    request = client.spreadsheets().values().update(
        spreadsheetId =
            object_id,
        valueInputOption = 'USER_ENTERED',
        range =
            range_a1,
        body = { 'values': region }
    )
    request.execute()


def write_regions_to_google_spreadsheets_object(
    client,
    object_id,
    ranges_a1,
    regions
):
    request = client.spreadsheets().values().batchUpdate(
        spreadsheetId =
            object_id,
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': list(
                map(
                    lambda range_a1_region: {
                        'range':
                            range_a1_region[0],
                        'values': range_a1_region[1]
                    },
                    zip(
                        ranges_a1,
                        regions
                    )
                )
            )
        }
    )
    request.execute()


def clear_regions_in_google_spreadsheets_object(
    client,
    object_id,
    ranges_a1
):
    request = client.spreadsheets().values().batchClear(
        spreadsheetId =
            object_id,
        body = {
            'ranges':\
                ranges_a1
        }
    )
    request.execute()