# EMA Hourly Continuation — YFI/USDT P89_100

**Symbol:** YFI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.3711 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.6946 |
| gross_win_rate | 0.4049 |
| sharpe_ratio | -3.7415 |
| sortino_ratio | -0.6912 |
| max_drawdown | 0.5625 |
| cagr | -0.2748 |
| net_avg_win | 49.6537 |
| net_avg_loss | -91.0355 |
| avg_hold_time_bars | 4.8589 |
| exposure | 0.0358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
