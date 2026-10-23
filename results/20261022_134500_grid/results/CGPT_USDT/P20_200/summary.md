# EMA Hourly Continuation — CGPT/USDT P20_200

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6887 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -2.3133 |
| sortino_ratio | -0.6411 |
| max_drawdown | 0.5411 |
| cagr | -0.2621 |
| net_avg_win | 62.8380 |
| net_avg_loss | -86.1958 |
| avg_hold_time_bars | 35.2661 |
| exposure | 0.6204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
