# EMA Hourly Continuation — KNC/USDT P21_50

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.5433 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 1.0041 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -7.0969 |
| sortino_ratio | -3.0088 |
| max_drawdown | 0.9745 |
| cagr | -0.7661 |
| net_avg_win | 28.8988 |
| net_avg_loss | -43.3498 |
| avg_hold_time_bars | 6.3572 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
