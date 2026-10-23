# EMA Hourly Continuation — AXL/USDT P21_34

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1207 |
| net_profit_factor | 0.4282 |
| net_win_rate | 0.3828 |
| gross_profit_factor | 0.8719 |
| gross_win_rate | 0.4043 |
| sharpe_ratio | -11.4763 |
| sortino_ratio | -5.6325 |
| max_drawdown | 0.9993 |
| cagr | -0.9415 |
| net_avg_win | 16.1939 |
| net_avg_loss | -23.4548 |
| avg_hold_time_bars | 2.8583 |
| exposure | 0.1561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
