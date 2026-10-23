# EMA Hourly Continuation — VELO/USDT P34_89

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6619 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -3.5814 |
| sortino_ratio | -1.3557 |
| max_drawdown | 0.8113 |
| cagr | -0.4727 |
| net_avg_win | 44.8431 |
| net_avg_loss | -64.4300 |
| avg_hold_time_bars | 7.2989 |
| exposure | 0.2375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
