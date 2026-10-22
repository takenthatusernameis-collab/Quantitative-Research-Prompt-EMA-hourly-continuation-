# EMA Hourly Continuation — CSPR/USDT P12_34

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6558 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8491 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -3.4829 |
| sortino_ratio | -1.1099 |
| max_drawdown | 0.7230 |
| cagr | -0.4002 |
| net_avg_win | 62.0450 |
| net_avg_loss | -74.4816 |
| avg_hold_time_bars | 7.0000 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
