# EMA Hourly Continuation — API3/USDT P21_34

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.4557 |
| net_win_rate | 0.4203 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -10.3634 |
| sortino_ratio | -5.0677 |
| max_drawdown | 0.9983 |
| cagr | -0.9205 |
| net_avg_win | 16.7825 |
| net_avg_loss | -26.6963 |
| avg_hold_time_bars | 2.7553 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
