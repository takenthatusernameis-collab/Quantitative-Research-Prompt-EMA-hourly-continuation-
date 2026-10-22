# EMA Hourly Continuation — MOCA/USDT P21_34

**Symbol:** MOCA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6227 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9009 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -2.7796 |
| sortino_ratio | -0.7219 |
| max_drawdown | 0.5751 |
| cagr | -0.2816 |
| net_avg_win | 61.9209 |
| net_avg_loss | -88.7418 |
| avg_hold_time_bars | 4.7826 |
| exposure | 0.0717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
