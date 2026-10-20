# EMA Hourly Continuation — IOTX/USDT P100_200

**Symbol:** IOTX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.5930 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -3.1649 |
| sortino_ratio | -0.9556 |
| max_drawdown | 0.6859 |
| cagr | -0.3639 |
| net_avg_win | 44.7505 |
| net_avg_loss | -70.9731 |
| avg_hold_time_bars | 8.1842 |
| exposure | 0.1696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
