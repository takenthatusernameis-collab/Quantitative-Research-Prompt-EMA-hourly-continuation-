# EMA Hourly Continuation — GRT/USDT P20_50

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.4970 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8444 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -7.0969 |
| sortino_ratio | -3.1473 |
| max_drawdown | 0.9801 |
| cagr | -0.7875 |
| net_avg_win | 21.4640 |
| net_avg_loss | -35.4166 |
| avg_hold_time_bars | 4.3806 |
| exposure | 0.1984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
