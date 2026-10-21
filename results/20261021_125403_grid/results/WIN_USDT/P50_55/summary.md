# EMA Hourly Continuation — WIN/USDT P50_55

**Symbol:** WIN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 95 |
| net_profit_factor | 0.7000 |
| net_win_rate | 0.5368 |
| gross_profit_factor | 1.1591 |
| gross_win_rate | 0.5368 |
| sharpe_ratio | -1.0502 |
| sortino_ratio | -0.1487 |
| max_drawdown | 0.1881 |
| cagr | -0.0653 |
| net_avg_win | 71.3819 |
| net_avg_loss | -118.1967 |
| avg_hold_time_bars | 5.5895 |
| exposure | 0.0241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
