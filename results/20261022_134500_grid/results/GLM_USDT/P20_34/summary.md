# EMA Hourly Continuation — GLM/USDT P20_34

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1084 |
| net_profit_factor | 0.3982 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.9075 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -10.3767 |
| sortino_ratio | -4.8613 |
| max_drawdown | 0.9979 |
| cagr | -0.9141 |
| net_avg_win | 14.7384 |
| net_avg_loss | -26.0720 |
| avg_hold_time_bars | 3.5720 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
