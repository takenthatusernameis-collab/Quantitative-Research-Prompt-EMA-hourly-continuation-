# EMA Hourly Continuation — ONDO/USDT P26_144

**Symbol:** ONDO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.8466 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.0582 |
| sortino_ratio | -0.2960 |
| max_drawdown | 0.4271 |
| cagr | -0.1289 |
| net_avg_win | 85.0605 |
| net_avg_loss | -99.4281 |
| avg_hold_time_bars | 21.8979 |
| exposure | 0.3802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
