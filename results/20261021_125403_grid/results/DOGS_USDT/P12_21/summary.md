# EMA Hourly Continuation — DOGS/USDT P12_21

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.7195 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -1.4848 |
| sortino_ratio | -0.3216 |
| max_drawdown | 0.3114 |
| cagr | -0.1369 |
| net_avg_win | 72.5258 |
| net_avg_loss | -96.7682 |
| avg_hold_time_bars | 4.6582 |
| exposure | 0.0484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
