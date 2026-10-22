# EMA Hourly Continuation — SQD/USDT P20_21

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 187 |
| net_profit_factor | 0.7723 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.1182 |
| sortino_ratio | -0.2229 |
| max_drawdown | 0.2837 |
| cagr | -0.0972 |
| net_avg_win | 79.3746 |
| net_avg_loss | -103.8797 |
| avg_hold_time_bars | 4.6952 |
| exposure | 0.0413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
