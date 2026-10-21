# EMA Hourly Continuation — ALGO/USDT P20_21

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 99 |
| net_profit_factor | 0.5401 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.7789 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -1.9380 |
| sortino_ratio | -0.2758 |
| max_drawdown | 0.2985 |
| cagr | -0.1193 |
| net_avg_win | 74.6312 |
| net_avg_loss | -106.0985 |
| avg_hold_time_bars | 4.1212 |
| exposure | 0.0185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
