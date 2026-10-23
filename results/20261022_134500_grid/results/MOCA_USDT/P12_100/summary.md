# EMA Hourly Continuation — MOCA/USDT P12_100

**Symbol:** MOCA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.6036 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8953 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -4.1994 |
| sortino_ratio | -1.5179 |
| max_drawdown | 0.8185 |
| cagr | -0.5134 |
| net_avg_win | 44.6266 |
| net_avg_loss | -63.3421 |
| avg_hold_time_bars | 18.4765 |
| exposure | 0.5520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
