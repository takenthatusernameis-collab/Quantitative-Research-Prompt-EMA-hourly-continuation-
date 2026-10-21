# EMA Hourly Continuation — HTX/USDT P8_20

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.4041 |
| net_win_rate | 0.3580 |
| gross_profit_factor | 0.7305 |
| gross_win_rate | 0.3657 |
| sharpe_ratio | -9.1836 |
| sortino_ratio | -3.4101 |
| max_drawdown | 0.9837 |
| cagr | -0.8037 |
| net_avg_win | 28.7427 |
| net_avg_loss | -39.6722 |
| avg_hold_time_bars | 6.1389 |
| exposure | 0.1800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
