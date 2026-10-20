# EMA Hourly Continuation — SWFTC/USDT P20_26

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1121 |
| net_profit_factor | 0.1269 |
| net_win_rate | 0.3149 |
| gross_profit_factor | 0.4456 |
| gross_win_rate | 0.3506 |
| sharpe_ratio | -15.7320 |
| sortino_ratio | -7.7040 |
| max_drawdown | 1.0000 |
| cagr | -0.9867 |
| net_avg_win | 4.1183 |
| net_avg_loss | -14.9135 |
| avg_hold_time_bars | 2.1534 |
| exposure | 0.1097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
