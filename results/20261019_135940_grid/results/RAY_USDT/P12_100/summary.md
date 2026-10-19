# EMA Hourly Continuation — RAY/USDT P12_100

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6576 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.6365 |
| sortino_ratio | -1.3014 |
| max_drawdown | 0.8059 |
| cagr | -0.4663 |
| net_avg_win | 49.1504 |
| net_avg_loss | -66.7738 |
| avg_hold_time_bars | 18.2146 |
| exposure | 0.5440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
