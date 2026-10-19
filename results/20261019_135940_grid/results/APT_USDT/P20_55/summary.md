# EMA Hourly Continuation — APT/USDT P20_55

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 977 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -6.4017 |
| sortino_ratio | -2.8296 |
| max_drawdown | 0.9697 |
| cagr | -0.7452 |
| net_avg_win | 22.2690 |
| net_avg_loss | -38.0651 |
| avg_hold_time_bars | 5.3347 |
| exposure | 0.2369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
