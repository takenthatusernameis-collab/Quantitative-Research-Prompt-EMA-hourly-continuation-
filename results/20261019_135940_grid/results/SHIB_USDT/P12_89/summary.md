# EMA Hourly Continuation — SHIB/USDT P12_89

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 835 |
| net_profit_factor | 0.6007 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.9522 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -5.8724 |
| sortino_ratio | -2.3695 |
| max_drawdown | 0.9497 |
| cagr | -0.6923 |
| net_avg_win | 37.3409 |
| net_avg_loss | -52.4196 |
| avg_hold_time_bars | 12.6778 |
| exposure | 0.4812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
