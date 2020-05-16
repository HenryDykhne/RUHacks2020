$(document).ready(function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['timeGrid', 'dayGrid', 'interaction'],
        defaultView: 'timeGridWeek',
        events: [
            {
                title: 'Walmart Shopping',
                start: '2020-05-16'
            }
        ],
        dateClick: function (info) {
            $('#eventModal').modal('show');
            $('#addButton').click(function () {
                var name = document.getElementById('eventName').value;
                var endDate = document.getElementById('endDate').value;
                calendar.addEvent({
                    title: name,
                    start: info.dateStr,
                    end: endDate
                });
            });
            document.getElementById('eventForm').reset();
        }
    });

    calendar.render();
});