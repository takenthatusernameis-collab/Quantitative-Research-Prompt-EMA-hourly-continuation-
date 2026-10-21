# EMA Hourly Continuation — ETHFI/USDT P8_12

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.7728 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 0.9923 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -1.0838 |
| sortino_ratio | -0.2238 |
| max_drawdown | 0.2692 |
| cagr | -0.0979 |
| net_avg_win | 74.5335 |
| net_avg_loss | -97.3873 |
| avg_hold_time_bars | 3.9662 |
| exposure | 0.0373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
