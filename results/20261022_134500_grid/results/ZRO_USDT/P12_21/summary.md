# EMA Hourly Continuation — ZRO/USDT P12_21

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1420 |
| net_profit_factor | 0.3746 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.7681 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -12.0859 |
| sortino_ratio | -6.6789 |
| max_drawdown | 0.9996 |
| cagr | -0.9665 |
| net_avg_win | 10.0647 |
| net_avg_loss | -19.3756 |
| avg_hold_time_bars | 2.0620 |
| exposure | 0.1433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
