# EMA Hourly Continuation — LISTA/USDT P8_55

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.5358 |
| sortino_ratio | -0.9381 |
| max_drawdown | 0.6730 |
| cagr | -0.3509 |
| net_avg_win | 62.6331 |
| net_avg_loss | -76.0050 |
| avg_hold_time_bars | 15.6995 |
| exposure | 0.4829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
