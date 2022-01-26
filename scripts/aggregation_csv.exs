defmodule AggregationCsv do
  def trim(argv) do
    [pub_file, sub_file, out_file] = argv
    trim_result(pub_file, sub_file, out_file)
  end

  def trim_result(pub_file, sub_file, out_file) do
    pub_rows = trim_csv(pub_file)
    sub_rows = trim_csv(sub_file)

    File.write(out_file, "")

    for [pub_msg, pub_time] <- pub_rows do
      result = "#{pub_msg}"
      File.write(out_file, result, [:append])

      for [sub_msg, sub_time] <- sub_rows do
        if pub_msg == sub_msg do
          result = ",#{sub_time - pub_time}"
          File.write(out_file, result, [:append])
        end
      end

      File.write(out_file, "\r\n", [:append])
    end
  end

  defp trim_csv(file) do
    rows =
      file
      |> File.stream!()
      |> Stream.map(&String.trim(&1))
      |> Stream.map(&String.split(&1, ","))
      |> Enum.to_list()

    Enum.map(rows, fn [msg, time_string] ->
      time = String.to_integer(time_string)
      [msg, time]
    end)
  end
end

AggregationCsv.trim(System.argv())
