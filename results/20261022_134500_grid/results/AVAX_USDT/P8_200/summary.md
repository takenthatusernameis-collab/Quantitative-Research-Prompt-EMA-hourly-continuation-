# EMA Hourly Continuation — AVAX/USDT P8_200

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6956 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -2.2318 |
| sortino_ratio | -0.5714 |
| max_drawdown | 0.5335 |
| cagr | -0.2419 |
| net_avg_win | 71.1453 |
| net_avg_loss | -94.6311 |
| avg_hold_time_bars | 53.0836 |
| exposure | 0.8083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
