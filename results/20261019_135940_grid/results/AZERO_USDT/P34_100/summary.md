# EMA Hourly Continuation — AZERO/USDT P34_100

**Symbol:** AZERO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6094 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -3.4407 |
| sortino_ratio | -1.1281 |
| max_drawdown | 0.7559 |
| cagr | -0.4223 |
| net_avg_win | 43.9513 |
| net_avg_loss | -67.5553 |
| avg_hold_time_bars | 12.4255 |
| exposure | 0.3092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
