document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var arr = [
        {
            title: 'Shopping at Walmart',
            start: '2020-05-16'
        }
    ]

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['timeGrid', 'dayGrid', 'interaction', 'bootstrap', 'googleCalendar'],
        googleCalendarApiKey: 'AIzaSyD3-iMIisR49ogp0kdaY7Snf7MUyeBb3PM',
        defaultView: 'timeGridWeek',
        themeSystem: 'bootstrap',
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
            $('#delButton').click(function() {
                info.event.remove();
            });
        },
        events: 'utexas.edu_g7oiojf3mkslee5cgq0ocn0ck4@group.calendar.google.com'
        //events: arr
    });

    calendar.render();
});