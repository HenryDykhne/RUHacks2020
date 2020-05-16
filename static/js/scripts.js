document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['timeGrid', 'dayGrid', 'interaction'],
        defaultView: 'timeGridWeek',
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
        events: [
            {
                title: 'Walmart Shopping',
                start: '2020-05-16'
            }
        ]
    });

    calendar.render();
});