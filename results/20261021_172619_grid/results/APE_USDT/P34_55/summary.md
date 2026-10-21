# EMA Hourly Continuation — APE/USDT P34_55

**Symbol:** APE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7811 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.0806 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -1.3453 |
| sortino_ratio | -0.3344 |
| max_drawdown | 0.3376 |
| cagr | -0.1414 |
| net_avg_win | 73.6957 |
| net_avg_loss | -101.6102 |
| avg_hold_time_bars | 5.1145 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
