# EMA Hourly Continuation — JASMY/USDT P12_50

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.5193 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.8293 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -6.4373 |
| sortino_ratio | -3.0099 |
| max_drawdown | 0.9760 |
| cagr | -0.7685 |
| net_avg_win | 20.4036 |
| net_avg_loss | -34.1901 |
| avg_hold_time_bars | 6.5978 |
| exposure | 0.3326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
