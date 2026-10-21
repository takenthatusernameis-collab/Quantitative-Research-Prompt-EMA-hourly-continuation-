# EMA Hourly Continuation — MERL/USDT P12_20

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7455 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7118 |
| sortino_ratio | -0.4766 |
| max_drawdown | 0.4314 |
| cagr | -0.1962 |
| net_avg_win | 65.9844 |
| net_avg_loss | -87.5762 |
| avg_hold_time_bars | 4.6782 |
| exposure | 0.0802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
