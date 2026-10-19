# EMA Hourly Continuation — TRX/USDT P8_50

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 957 |
| net_profit_factor | 0.3848 |
| net_win_rate | 0.4096 |
| gross_profit_factor | 1.1135 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -11.2684 |
| sortino_ratio | -4.9863 |
| max_drawdown | 0.9988 |
| cagr | -0.9313 |
| net_avg_win | 15.9370 |
| net_avg_loss | -28.7350 |
| avg_hold_time_bars | 10.2905 |
| exposure | 0.4476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
