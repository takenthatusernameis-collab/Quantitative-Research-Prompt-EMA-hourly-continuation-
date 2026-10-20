# EMA Hourly Continuation — SAFE/USDT P20_100

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6368 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9390 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -3.6754 |
| sortino_ratio | -1.3287 |
| max_drawdown | 0.8179 |
| cagr | -0.4681 |
| net_avg_win | 44.6835 |
| net_avg_loss | -63.9987 |
| avg_hold_time_bars | 14.1227 |
| exposure | 0.4217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
