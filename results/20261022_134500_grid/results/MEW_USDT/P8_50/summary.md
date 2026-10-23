# EMA Hourly Continuation — MEW/USDT P8_50

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -5.3540 |
| sortino_ratio | -2.4672 |
| max_drawdown | 0.9500 |
| cagr | -0.6904 |
| net_avg_win | 33.1947 |
| net_avg_loss | -45.7752 |
| avg_hold_time_bars | 9.1174 |
| exposure | 0.4447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
