# EMA Hourly Continuation — SUI/USDT P20_50

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7929 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0212 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.6414 |
| sortino_ratio | -0.4991 |
| max_drawdown | 0.4938 |
| cagr | -0.2048 |
| net_avg_win | 74.1182 |
| net_avg_loss | -94.7371 |
| avg_hold_time_bars | 8.4588 |
| exposure | 0.1726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
