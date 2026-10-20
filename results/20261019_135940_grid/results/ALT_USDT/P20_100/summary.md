# EMA Hourly Continuation — ALT/USDT P20_100

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6635 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.1092 |
| sortino_ratio | -1.0688 |
| max_drawdown | 0.7296 |
| cagr | -0.3929 |
| net_avg_win | 50.3176 |
| net_avg_loss | -68.7177 |
| avg_hold_time_bars | 16.8472 |
| exposure | 0.4510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
