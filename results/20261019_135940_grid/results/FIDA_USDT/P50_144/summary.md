# EMA Hourly Continuation — FIDA/USDT P50_144

**Symbol:** FIDA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.5795 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8740 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -3.6705 |
| sortino_ratio | -1.1913 |
| max_drawdown | 0.7624 |
| cagr | -0.4284 |
| net_avg_win | 42.1859 |
| net_avg_loss | -63.9872 |
| avg_hold_time_bars | 11.9867 |
| exposure | 0.2864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
