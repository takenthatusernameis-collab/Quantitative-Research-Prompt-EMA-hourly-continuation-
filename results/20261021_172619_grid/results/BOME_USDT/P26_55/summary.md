# EMA Hourly Continuation — BOME/USDT P26_55

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7913 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.3433 |
| sortino_ratio | -0.3906 |
| max_drawdown | 0.4376 |
| cagr | -0.1655 |
| net_avg_win | 66.5623 |
| net_avg_loss | -86.6146 |
| avg_hold_time_bars | 6.9024 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
