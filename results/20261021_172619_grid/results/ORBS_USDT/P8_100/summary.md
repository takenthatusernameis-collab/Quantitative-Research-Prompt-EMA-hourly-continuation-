# EMA Hourly Continuation — ORBS/USDT P8_100

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6976 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -3.2069 |
| sortino_ratio | -1.0730 |
| max_drawdown | 0.7211 |
| cagr | -0.3898 |
| net_avg_win | 63.7985 |
| net_avg_loss | -78.8710 |
| avg_hold_time_bars | 25.2937 |
| exposure | 0.6381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
