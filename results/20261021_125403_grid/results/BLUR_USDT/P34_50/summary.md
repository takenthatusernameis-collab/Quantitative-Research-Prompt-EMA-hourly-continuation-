# EMA Hourly Continuation — BLUR/USDT P34_50

**Symbol:** BLUR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7738 |
| net_win_rate | 0.5344 |
| gross_profit_factor | 1.1326 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -1.3183 |
| sortino_ratio | -0.3402 |
| max_drawdown | 0.3645 |
| cagr | -0.1439 |
| net_avg_win | 64.8585 |
| net_avg_loss | -96.1998 |
| avg_hold_time_bars | 4.5563 |
| exposure | 0.0660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
