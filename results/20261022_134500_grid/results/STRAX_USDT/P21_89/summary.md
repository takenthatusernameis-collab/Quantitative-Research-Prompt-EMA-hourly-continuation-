# EMA Hourly Continuation — STRAX/USDT P21_89

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 790 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.8204 |
| gross_win_rate | 0.4241 |
| sharpe_ratio | -7.1743 |
| sortino_ratio | -2.8411 |
| max_drawdown | 0.9691 |
| cagr | -0.7511 |
| net_avg_win | 33.5282 |
| net_avg_loss | -43.9379 |
| avg_hold_time_bars | 10.6544 |
| exposure | 0.3848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
