import { Logo } from "../../Logo";
import styled from "styled-components";
import { Inline } from "../../Inline";
import { Pad } from "../../Pad";

const Item = styled(Inline).attrs(() => ({
  as: Pad,
  gutter: "1rem",
  justify: "start",
  align: "center",
}))`
  text-align: left;
  color: black;
  margin: 0 0 0.5rem;
  flex-wrap: wrap;
  word-break: break-all;
`;

const Test = styled(Pad).attrs(() => ({
  gutter: "1rem",
}))`
  display: flex;
  color: gray;
  flex-direction: column;
`;
export default function Schema({ name, info,image }) {
  return (
    <Test>
      <Item>
        <Logo size={"15px"} square>
          <img
            style={{ width: "18px", height: "18px" }}
            alt={"code"}
            src={require(`../../../assets/${image}.png`)}
          />
        </Logo>
        {name}
      </Item>
      {info}
    </Test>
  );
}
