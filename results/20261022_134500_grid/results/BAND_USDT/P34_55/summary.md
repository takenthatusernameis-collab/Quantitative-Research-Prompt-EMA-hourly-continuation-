# EMA Hourly Continuation — BAND/USDT P34_55

**Symbol:** BAND/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.4992 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9759 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -6.3908 |
| sortino_ratio | -2.5661 |
| max_drawdown | 0.9602 |
| cagr | -0.7144 |
| net_avg_win | 25.2538 |
| net_avg_loss | -44.2642 |
| avg_hold_time_bars | 4.3099 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
