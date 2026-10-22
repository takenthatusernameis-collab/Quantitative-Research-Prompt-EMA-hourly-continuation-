# EMA Hourly Continuation — ZPAY/USDT P55_100

**Symbol:** ZPAY/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.3985 |
| net_win_rate | 0.3523 |
| gross_profit_factor | 0.5768 |
| gross_win_rate | 0.3555 |
| sharpe_ratio | -6.7659 |
| sortino_ratio | -2.3518 |
| max_drawdown | 0.9404 |
| cagr | -0.6693 |
| net_avg_win | 28.6538 |
| net_avg_loss | -39.1093 |
| avg_hold_time_bars | 10.3377 |
| exposure | 0.2882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
