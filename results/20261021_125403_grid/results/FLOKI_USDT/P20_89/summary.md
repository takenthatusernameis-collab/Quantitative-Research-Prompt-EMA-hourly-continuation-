# EMA Hourly Continuation — FLOKI/USDT P20_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.7370 |
| sortino_ratio | -0.5534 |
| max_drawdown | 0.5040 |
| cagr | -0.2253 |
| net_avg_win | 68.9069 |
| net_avg_loss | -85.1603 |
| avg_hold_time_bars | 17.8712 |
| exposure | 0.4037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
