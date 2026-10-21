# EMA Hourly Continuation — AMP/USDT P8_21

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.4497 |
| net_win_rate | 0.3931 |
| gross_profit_factor | 0.6642 |
| gross_win_rate | 0.3931 |
| sharpe_ratio | -6.3231 |
| sortino_ratio | -2.2238 |
| max_drawdown | 0.9271 |
| cagr | -0.6436 |
| net_avg_win | 31.6319 |
| net_avg_loss | -45.5566 |
| avg_hold_time_bars | 4.9556 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
