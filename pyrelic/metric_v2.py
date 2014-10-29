class MetricV2(object):
    """
    An object to contain the data for one time period in a "get_instance_metric_data_v2"
    call. The properties are dynamic and based off the field names in the XML
    response
    """
    def __init__(self, timeslice, values):
        super(MetricV2, self).__init__()
        
        # Set the from and to datetime other than the selected values
        setattr(self, 'begin', timeslice.find('.//from').text)
        setattr(self, 'end', timeslice.find('.//to').text)
        
        # Attributes of the <timeslice> tag
        for k, v in timeslice.items():
            setattr(self, k, v)

        # All the selected fields if exist
        for value in values:
            for field in timeslice.findall(".//{0}".format(value)):
                # Each field has a 'name=metric_type' section.
                # We want to have this accessible in the object by calling the
                # metric_type property of the object directly
                setattr(self, value, field.text)
