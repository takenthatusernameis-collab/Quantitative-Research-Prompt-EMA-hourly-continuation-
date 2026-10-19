# EMA Hourly Continuation — DOGE/USDT P8_26

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1552 |
| net_profit_factor | 0.4094 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -11.5626 |
| sortino_ratio | -6.3790 |
| max_drawdown | 0.9998 |
| cagr | -0.9637 |
| net_avg_win | 10.2531 |
| net_avg_loss | -19.3250 |
| avg_hold_time_bars | 3.5039 |
| exposure | 0.2472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
