# EMA Hourly Continuation — DUSK/USDT P8_34

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.7973 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.6436 |
| sortino_ratio | -1.0739 |
| max_drawdown | 0.7746 |
| cagr | -0.3903 |
| net_avg_win | 71.1749 |
| net_avg_loss | -84.3394 |
| avg_hold_time_bars | 8.6724 |
| exposure | 0.3189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
