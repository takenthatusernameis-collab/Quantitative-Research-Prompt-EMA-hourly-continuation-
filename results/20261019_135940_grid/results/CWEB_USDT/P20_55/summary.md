# EMA Hourly Continuation — CWEB/USDT P20_55

**Symbol:** CWEB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.3811 |
| net_win_rate | 0.3365 |
| gross_profit_factor | 0.7277 |
| gross_win_rate | 0.3531 |
| sharpe_ratio | -11.6063 |
| sortino_ratio | -4.8178 |
| max_drawdown | 0.9985 |
| cagr | -0.9241 |
| net_avg_win | 21.6448 |
| net_avg_loss | -28.8066 |
| avg_hold_time_bars | 7.4408 |
| exposure | 0.2855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
