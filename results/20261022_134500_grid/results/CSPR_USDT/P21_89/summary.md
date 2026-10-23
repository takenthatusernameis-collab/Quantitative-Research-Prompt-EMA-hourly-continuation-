# EMA Hourly Continuation — CSPR/USDT P21_89

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.4399 |
| net_win_rate | 0.4126 |
| gross_profit_factor | 0.7627 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -7.8285 |
| sortino_ratio | -3.4726 |
| max_drawdown | 0.9869 |
| cagr | -0.8187 |
| net_avg_win | 18.7521 |
| net_avg_loss | -29.9443 |
| avg_hold_time_bars | 7.8571 |
| exposure | 0.3575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
