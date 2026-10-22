# EMA Hourly Continuation — DASH/USDT P55_100

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.3742 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.7894 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -6.4393 |
| sortino_ratio | -2.3267 |
| max_drawdown | 0.9469 |
| cagr | -0.6840 |
| net_avg_win | 19.4110 |
| net_avg_loss | -41.5831 |
| avg_hold_time_bars | 4.7125 |
| exposure | 0.1401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
