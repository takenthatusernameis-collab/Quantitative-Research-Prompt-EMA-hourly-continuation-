# EMA Hourly Continuation — VET/USDT P89_100

**Symbol:** VET/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.2536 |
| net_win_rate | 0.4094 |
| gross_profit_factor | 0.8342 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -8.7381 |
| sortino_ratio | -3.0775 |
| max_drawdown | 0.9835 |
| cagr | -0.8032 |
| net_avg_win | 13.6912 |
| net_avg_loss | -37.4202 |
| avg_hold_time_bars | 2.1426 |
| exposure | 0.0580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
