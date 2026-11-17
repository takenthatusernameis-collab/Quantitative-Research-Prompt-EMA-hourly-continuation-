# EMA Hourly Continuation — NUM/USDT P50_89

**Symbol:** NUM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.4512 |
| net_win_rate | 0.3814 |
| gross_profit_factor | 0.7684 |
| gross_win_rate | 0.3873 |
| sharpe_ratio | -7.4962 |
| sortino_ratio | -2.7551 |
| max_drawdown | 0.9662 |
| cagr | -0.7372 |
| net_avg_win | 30.6372 |
| net_avg_loss | -41.8721 |
| avg_hold_time_bars | 6.4183 |
| exposure | 0.1981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
