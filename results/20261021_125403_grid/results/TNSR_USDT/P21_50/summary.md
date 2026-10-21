# EMA Hourly Continuation — TNSR/USDT P21_50

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.8087 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0524 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.7008 |
| sortino_ratio | -0.5608 |
| max_drawdown | 0.5274 |
| cagr | -0.2276 |
| net_avg_win | 74.9532 |
| net_avg_loss | -96.6207 |
| avg_hold_time_bars | 7.7316 |
| exposure | 0.1851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
