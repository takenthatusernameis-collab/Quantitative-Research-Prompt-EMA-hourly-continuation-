# EMA Hourly Continuation — SQD/USDT P20_34

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1084 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -7.8964 |
| sortino_ratio | -3.7133 |
| max_drawdown | 0.9887 |
| cagr | -0.8421 |
| net_avg_win | 25.5973 |
| net_avg_loss | -37.4420 |
| avg_hold_time_bars | 2.8967 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
