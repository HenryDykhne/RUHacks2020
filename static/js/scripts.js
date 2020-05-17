document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var arr = [
        {
            id: '1',
            title: 'Shopping at Walmart',
            start: '2020-05-16',
            end: '2020-05-17',
            location: 'University of Calgary'
        },
        {
            id: '2',
            title: 'Eat at McDonalds',
            start: '2020-05-17',
            end: '2020-05-18',
            location: 'UT Austin'
        },
        {
            id: '3',
            title: 'Go to the beach',
            start: '2020-05-18',
            end: '2020-05-19',
            location: 'University of Berkeley'
        }
    ]

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['timeGrid', 'dayGrid', 'interaction', 'bootstrap', 'googleCalendar'],
        googleCalendarApiKey: 'AIzaSyD3-iMIisR49ogp0kdaY7Snf7MUyeBb3PM',
        defaultView: 'timeGridWeek',
        themeSystem: 'bootstrap',
        selectable: true,
        header: {
            center: 'addEventButton'
        },
        customButtons: {
            addEventButton: {
                text: 'Add Event',
                click: function() {
                    $('#addModal').modal('show');
                    $('#addButton').click(function () {
                        var name = document.getElementById('eventName').value;
                        var startDate = document.getElementById('startDate').value;
                        var endDate = document.getElementById('endDate').value;
                        calendar.addEvent({
                            title: name,
                            start: startDate,
                            end: endDate
                        });
                    });
                    document.getElementById('eventForm').reset();
                }
            }
        },
        eventClick: function(info) {
            $('#editModal').modal('show');
            $('#routeButton').unbind().click(function() {
                var id = info.event.id;
                window.open("route" + id);
            });

            $('#delButton').click(function() {
                info.event.remove();
            });
        },
        events: arr
    });

    console.log(calendar.getEvents());
    calendar.render();
});