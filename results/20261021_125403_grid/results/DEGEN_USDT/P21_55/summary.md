# EMA Hourly Continuation — DEGEN/USDT P21_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 1.0044 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.5623 |
| sortino_ratio | -0.5013 |
| max_drawdown | 0.4666 |
| cagr | -0.2072 |
| net_avg_win | 79.1285 |
| net_avg_loss | -96.0155 |
| avg_hold_time_bars | 8.8068 |
| exposure | 0.2013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
