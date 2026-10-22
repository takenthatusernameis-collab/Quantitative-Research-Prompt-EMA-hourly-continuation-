# EMA Hourly Continuation — STRAX/USDT P8_50

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.6721 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.9103 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -4.0448 |
| sortino_ratio | -1.5936 |
| max_drawdown | 0.8516 |
| cagr | -0.5197 |
| net_avg_win | 48.4752 |
| net_avg_loss | -62.7601 |
| avg_hold_time_bars | 12.1284 |
| exposure | 0.4231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
