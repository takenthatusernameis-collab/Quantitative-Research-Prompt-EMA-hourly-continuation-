# EMA Hourly Continuation — SQD/USDT P8_12

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.3138 |
| net_win_rate | 0.3826 |
| gross_profit_factor | 0.7615 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -14.9062 |
| sortino_ratio | -8.5718 |
| max_drawdown | 1.0000 |
| cagr | -0.9896 |
| net_avg_win | 7.4848 |
| net_avg_loss | -14.7800 |
| avg_hold_time_bars | 1.9624 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
