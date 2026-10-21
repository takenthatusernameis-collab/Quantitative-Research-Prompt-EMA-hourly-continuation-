# EMA Hourly Continuation — AAVE/USDT P20_50

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6644 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.8232 |
| sortino_ratio | -0.8597 |
| max_drawdown | 0.6320 |
| cagr | -0.3254 |
| net_avg_win | 58.6327 |
| net_avg_loss | -76.6749 |
| avg_hold_time_bars | 8.1053 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
