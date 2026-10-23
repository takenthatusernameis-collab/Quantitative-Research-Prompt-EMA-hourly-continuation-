# EMA Hourly Continuation — VR/USDT P8_89

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 855 |
| net_profit_factor | 0.5504 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.8131 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -7.4552 |
| sortino_ratio | -2.9621 |
| max_drawdown | 0.9832 |
| cagr | -0.8022 |
| net_avg_win | 33.2436 |
| net_avg_loss | -44.3478 |
| avg_hold_time_bars | 15.2164 |
| exposure | 0.5914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
