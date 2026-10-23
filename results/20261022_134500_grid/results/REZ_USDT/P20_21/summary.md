# EMA Hourly Continuation — REZ/USDT P20_21

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1127 |
| net_profit_factor | 0.2530 |
| net_win_rate | 0.3478 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -14.5881 |
| sortino_ratio | -7.2004 |
| max_drawdown | 0.9999 |
| cagr | -0.9801 |
| net_avg_win | 8.6399 |
| net_avg_loss | -18.2126 |
| avg_hold_time_bars | 2.1437 |
| exposure | 0.1115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
