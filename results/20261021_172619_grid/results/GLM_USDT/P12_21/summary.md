# EMA Hourly Continuation — GLM/USDT P12_21

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.5977 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9747 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -3.9601 |
| sortino_ratio | -1.3520 |
| max_drawdown | 0.7891 |
| cagr | -0.4604 |
| net_avg_win | 42.2442 |
| net_avg_loss | -68.9370 |
| avg_hold_time_bars | 4.8984 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
