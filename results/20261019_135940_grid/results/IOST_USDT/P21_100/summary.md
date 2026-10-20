# EMA Hourly Continuation — IOST/USDT P21_100

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.6180 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 1.0134 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -3.7944 |
| sortino_ratio | -1.3711 |
| max_drawdown | 0.8310 |
| cagr | -0.4911 |
| net_avg_win | 39.6716 |
| net_avg_loss | -63.6216 |
| avg_hold_time_bars | 13.0090 |
| exposure | 0.3956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
