# EMA Hourly Continuation — FIDA/USDT P26_34

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.5979 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9216 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -2.8418 |
| sortino_ratio | -0.7291 |
| max_drawdown | 0.5715 |
| cagr | -0.2853 |
| net_avg_win | 54.8184 |
| net_avg_loss | -85.0988 |
| avg_hold_time_bars | 5.1988 |
| exposure | 0.0758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
