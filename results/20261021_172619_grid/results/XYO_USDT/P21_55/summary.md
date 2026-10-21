# EMA Hourly Continuation — XYO/USDT P21_55

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6242 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -3.9875 |
| sortino_ratio | -1.3191 |
| max_drawdown | 0.7895 |
| cagr | -0.4557 |
| net_avg_win | 53.6094 |
| net_avg_loss | -70.2721 |
| avg_hold_time_bars | 8.1704 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
