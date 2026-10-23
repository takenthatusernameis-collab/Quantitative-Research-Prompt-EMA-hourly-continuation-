# EMA Hourly Continuation — UQC/USDT P100_200

**Symbol:** UQC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.2656 |
| net_win_rate | 0.2763 |
| gross_profit_factor | 0.5110 |
| gross_win_rate | 0.3074 |
| sharpe_ratio | -6.9548 |
| sortino_ratio | -1.5891 |
| max_drawdown | 0.8880 |
| cagr | -0.5803 |
| net_avg_win | 45.2325 |
| net_avg_loss | -65.0099 |
| avg_hold_time_bars | 34.7977 |
| exposure | 0.4048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
