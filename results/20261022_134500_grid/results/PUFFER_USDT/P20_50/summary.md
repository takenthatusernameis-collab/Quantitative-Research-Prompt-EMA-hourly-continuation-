# EMA Hourly Continuation — PUFFER/USDT P20_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.6338 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9981 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -4.3559 |
| sortino_ratio | -1.8758 |
| max_drawdown | 0.8374 |
| cagr | -0.5922 |
| net_avg_win | 39.3338 |
| net_avg_loss | -60.2565 |
| avg_hold_time_bars | 5.3842 |
| exposure | 0.2276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
