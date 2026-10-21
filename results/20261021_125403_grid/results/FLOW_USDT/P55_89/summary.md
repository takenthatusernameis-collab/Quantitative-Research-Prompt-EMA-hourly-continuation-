# EMA Hourly Continuation — FLOW/USDT P55_89

**Symbol:** FLOW/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6509 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.3759 |
| sortino_ratio | -0.6119 |
| max_drawdown | 0.5211 |
| cagr | -0.2441 |
| net_avg_win | 60.7292 |
| net_avg_loss | -86.0746 |
| avg_hold_time_bars | 6.4303 |
| exposure | 0.0944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
