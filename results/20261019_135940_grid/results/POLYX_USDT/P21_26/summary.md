# EMA Hourly Continuation — POLYX/USDT P21_26

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1083 |
| net_profit_factor | 0.2336 |
| net_win_rate | 0.3638 |
| gross_profit_factor | 0.6943 |
| gross_win_rate | 0.4303 |
| sharpe_ratio | -13.1142 |
| sortino_ratio | -6.2575 |
| max_drawdown | 0.9997 |
| cagr | -0.9629 |
| net_avg_win | 7.7343 |
| net_avg_loss | -18.9329 |
| avg_hold_time_bars | 2.4912 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
