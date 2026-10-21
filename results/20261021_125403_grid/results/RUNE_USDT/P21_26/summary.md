# EMA Hourly Continuation — RUNE/USDT P21_26

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.5932 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.8915 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -1.9886 |
| sortino_ratio | -0.3683 |
| max_drawdown | 0.3562 |
| cagr | -0.1560 |
| net_avg_win | 63.2375 |
| net_avg_loss | -98.0217 |
| avg_hold_time_bars | 4.4012 |
| exposure | 0.0334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
