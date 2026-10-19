# EMA Hourly Continuation — BONK/USDT P20_26

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1179 |
| net_profit_factor | 0.3492 |
| net_win_rate | 0.3723 |
| gross_profit_factor | 0.7788 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -13.0100 |
| sortino_ratio | -6.4188 |
| max_drawdown | 0.9998 |
| cagr | -0.9660 |
| net_avg_win | 12.2190 |
| net_avg_loss | -20.7596 |
| avg_hold_time_bars | 1.9432 |
| exposure | 0.1041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
