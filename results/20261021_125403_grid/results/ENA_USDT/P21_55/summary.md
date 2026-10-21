# EMA Hourly Continuation — ENA/USDT P21_55

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.8846 |
| net_win_rate | 0.5198 |
| gross_profit_factor | 1.0683 |
| gross_win_rate | 0.5198 |
| sharpe_ratio | -0.7706 |
| sortino_ratio | -0.2428 |
| max_drawdown | 0.3657 |
| cagr | -0.1096 |
| net_avg_win | 77.8073 |
| net_avg_loss | -95.2289 |
| avg_hold_time_bars | 9.0021 |
| exposure | 0.1960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
