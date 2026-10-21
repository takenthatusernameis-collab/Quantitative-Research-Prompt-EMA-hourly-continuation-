# EMA Hourly Continuation — ID/USDT P12_26

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.6680 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.4960 |
| sortino_ratio | -1.2640 |
| max_drawdown | 0.7834 |
| cagr | -0.4405 |
| net_avg_win | 49.4228 |
| net_avg_loss | -70.8195 |
| avg_hold_time_bars | 5.6578 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
