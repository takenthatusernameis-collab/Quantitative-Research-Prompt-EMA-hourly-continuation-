# EMA Hourly Continuation — RUNE/USDT P26_55

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.8122 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1386 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -1.3395 |
| sortino_ratio | -0.3963 |
| max_drawdown | 0.3726 |
| cagr | -0.1664 |
| net_avg_win | 70.8024 |
| net_avg_loss | -99.6326 |
| avg_hold_time_bars | 7.7524 |
| exposure | 0.1480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
