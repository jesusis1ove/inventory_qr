import { Layers } from "../../Layers";
import styled from "styled-components";
import { Pad } from "../../Pad";
import Schema from "./schema";

const List = styled(Layers).attrs(() => ({
  as: "ul",
}))`
  list-style-type: none;
  @media (max-width: 1000px) {
    padding: 0;
    font-size: 14px;
  }
`;

export default function Info({ meterById }) {
  return (
    <Pad as={"nav"}>
      <List>
        <Schema name={"Номер"} info={meterById?.code} image={"id"} />
        <Schema
          name={"Дата последней поверки"}
          info={meterById?.verification_date}
          image={"check"}
        />
        <Schema
          name={"Направление"}
          info={meterById?.direction}
          image={"direction"}
        />
        <Schema
          name={"Межосевое расстояние"}
          info={meterById?.center_distance}
          image={"dimensions"}
        />
        <Schema
          name={"Межповерочный интервал"}
          image={"timetable"}
          info={meterById?.verification_interval}
        />
        <Schema name={"Адрес"} info={meterById?.address} image={"location"} />
      </List>
    </Pad>
  );
}
