# EMA Hourly Continuation — PIXEL/USDT P26_89

**Symbol:** PIXEL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.7064 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 1.0229 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -2.9662 |
| sortino_ratio | -1.1063 |
| max_drawdown | 0.7504 |
| cagr | -0.4061 |
| net_avg_win | 50.8725 |
| net_avg_loss | -70.9858 |
| avg_hold_time_bars | 10.2009 |
| exposure | 0.3217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
