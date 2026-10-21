# EMA Hourly Continuation — SQD/USDT P55_200

**Symbol:** SQD/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8969 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0464 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -0.6009 |
| sortino_ratio | -0.1557 |
| max_drawdown | 0.2446 |
| cagr | -0.0722 |
| net_avg_win | 89.8978 |
| net_avg_loss | -104.7839 |
| avg_hold_time_bars | 21.4603 |
| exposure | 0.3177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
