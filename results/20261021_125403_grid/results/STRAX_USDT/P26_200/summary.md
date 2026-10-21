# EMA Hourly Continuation — STRAX/USDT P26_200

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5842 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.7527 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -3.6727 |
| sortino_ratio | -1.1063 |
| max_drawdown | 0.7218 |
| cagr | -0.4010 |
| net_avg_win | 52.2795 |
| net_avg_loss | -67.2882 |
| avg_hold_time_bars | 24.0022 |
| exposure | 0.4960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
