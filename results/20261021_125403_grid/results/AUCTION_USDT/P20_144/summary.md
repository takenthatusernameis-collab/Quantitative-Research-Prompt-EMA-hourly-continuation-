# EMA Hourly Continuation — AUCTION/USDT P20_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6960 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9078 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.5608 |
| sortino_ratio | -0.7382 |
| max_drawdown | 0.6050 |
| cagr | -0.2919 |
| net_avg_win | 68.2376 |
| net_avg_loss | -86.1227 |
| avg_hold_time_bars | 29.9688 |
| exposure | 0.5656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
