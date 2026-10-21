# EMA Hourly Continuation — CPOOL/USDT P20_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7796 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -1.4549 |
| sortino_ratio | -0.4042 |
| max_drawdown | 0.4299 |
| cagr | -0.1714 |
| net_avg_win | 73.1789 |
| net_avg_loss | -84.9896 |
| avg_hold_time_bars | 31.5666 |
| exposure | 0.5495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
