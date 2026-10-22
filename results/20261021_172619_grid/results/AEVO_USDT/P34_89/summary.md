# EMA Hourly Continuation — AEVO/USDT P34_89

**Symbol:** AEVO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7231 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9205 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -2.1482 |
| sortino_ratio | -0.6834 |
| max_drawdown | 0.5543 |
| cagr | -0.2694 |
| net_avg_win | 59.0187 |
| net_avg_loss | -77.1603 |
| avg_hold_time_bars | 11.4036 |
| exposure | 0.2570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
