# EMA Hourly Continuation — TRAC/USDT P34_89

**Symbol:** TRAC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7567 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.6432 |
| sortino_ratio | -0.4823 |
| max_drawdown | 0.4785 |
| cagr | -0.1983 |
| net_avg_win | 63.0891 |
| net_avg_loss | -83.7699 |
| avg_hold_time_bars | 11.2029 |
| exposure | 0.2134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
