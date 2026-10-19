# EMA Hourly Continuation — KAS/USDT P12_26

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1485 |
| net_profit_factor | 0.3269 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.7967 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -10.8934 |
| sortino_ratio | -5.9007 |
| max_drawdown | 0.9995 |
| cagr | -0.9522 |
| net_avg_win | 7.3757 |
| net_avg_loss | -17.9545 |
| avg_hold_time_bars | 2.7596 |
| exposure | 0.1863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
