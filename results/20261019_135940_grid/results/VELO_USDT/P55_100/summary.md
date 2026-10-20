# EMA Hourly Continuation — VELO/USDT P55_100

**Symbol:** VELO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6354 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9378 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -3.7808 |
| sortino_ratio | -1.3829 |
| max_drawdown | 0.8159 |
| cagr | -0.4797 |
| net_avg_win | 43.6326 |
| net_avg_loss | -64.0904 |
| avg_hold_time_bars | 5.1544 |
| exposure | 0.1563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
