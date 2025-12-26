import React from "react";

function DivergenceView() {
  const [data, setData] = React.useState([]);
  const [error, setError] = React.useState(null);
  const [asOfDate, setAsOfDate] = React.useState("");

  function fetchData(date) {
    var url = "http://127.0.0.1:8000/divergences";
    if (date && date !== "") {
      url = "http://127.0.0.1:8000/divergences?as_of=" + date;
    }

    fetch(url)
      .then(function (res) {
        if (!res.ok) {
          throw new Error("Fetch failed");
        }
        return res.json();
      })
      .then(function (json) {
        setData(json);
        setError(null);
      })
      .catch(function (err) {
        setError(err.message);
      });
  }

  React.useEffect(function () {
    fetchData(asOfDate);
  }, [asOfDate]);

  return (
    <div>
      <h2>Divergence View</h2>

      <p>
        This view shows where different authorities assert incompatible values
        about the same subject. Selecting a date changes the historical lens.
        No resolution or judgment is performed.
      </p>

      <div>
        <label>View as of date: </label>
        <input
          type="date"
          value={asOfDate}
          onChange={function (e) {
            setAsOfDate(e.target.value);
          }}
        />
        {asOfDate !== "" ? (
          <button
            onClick={function () {
              setAsOfDate("");
            }}
          >
            Clear
          </button>
        ) : null}
      </div>

      {error ? <div>Error: {error}</div> : null}

      {data.length === 0 ? (
        <div>No divergences detected for the selected time.</div>
      ) : null}

      {data.map(function (d, idx) {
        return (
          <div key={idx}>
            <h3>
              {d.subject} ({d.predicate} · {d.object})
            </h3>

            <table>
              <thead>
                <tr>
                  <th>Authority</th>
                  <th>Assertion</th>
                  <th>Time</th>
                </tr>
              </thead>
              <tbody>
                {d.assertions.map(function (a, i) {
                  return (
                    <tr key={i}>
                      <td>{a.authority}</td>
                      <td>{a.value}</td>
                      <td>{a.asserted_at}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        );
      })}
    </div>
  );
}

export default DivergenceView;

