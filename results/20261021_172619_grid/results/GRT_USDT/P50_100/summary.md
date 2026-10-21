# EMA Hourly Continuation — GRT/USDT P50_100

**Symbol:** GRT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7922 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0515 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -1.3346 |
| sortino_ratio | -0.3664 |
| max_drawdown | 0.3915 |
| cagr | -0.1549 |
| net_avg_win | 69.7918 |
| net_avg_loss | -94.0672 |
| avg_hold_time_bars | 8.3415 |
| exposure | 0.1382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
