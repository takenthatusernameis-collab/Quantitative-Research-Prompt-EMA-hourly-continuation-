# EMA Hourly Continuation — TFUEL/USDT P8_26

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5996 |
| net_win_rate | 0.4284 |
| gross_profit_factor | 0.8570 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -5.6661 |
| sortino_ratio | -2.1931 |
| max_drawdown | 0.9227 |
| cagr | -0.6365 |
| net_avg_win | 43.5693 |
| net_avg_loss | -54.4517 |
| avg_hold_time_bars | 6.4014 |
| exposure | 0.2144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
