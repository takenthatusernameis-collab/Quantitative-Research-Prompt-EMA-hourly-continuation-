# EMA Hourly Continuation — CKB/USDT P26_100

**Symbol:** CKB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.7983 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.5202 |
| sortino_ratio | -0.4566 |
| max_drawdown | 0.4449 |
| cagr | -0.1907 |
| net_avg_win | 73.1346 |
| net_avg_loss | -94.5846 |
| avg_hold_time_bars | 17.5649 |
| exposure | 0.3505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
