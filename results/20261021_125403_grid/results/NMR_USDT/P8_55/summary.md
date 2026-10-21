# EMA Hourly Continuation — NMR/USDT P8_55

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 766 |
| net_profit_factor | 0.8632 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.1150 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -1.4488 |
| sortino_ratio | -0.5769 |
| max_drawdown | 0.5591 |
| cagr | -0.2361 |
| net_avg_win | 76.9550 |
| net_avg_loss | -98.9757 |
| avg_hold_time_bars | 12.3329 |
| exposure | 0.4294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
