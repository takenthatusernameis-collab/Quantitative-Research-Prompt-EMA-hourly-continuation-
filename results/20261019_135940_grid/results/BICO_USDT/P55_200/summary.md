# EMA Hourly Continuation — BICO/USDT P55_200

**Symbol:** BICO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6410 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8476 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -2.7096 |
| sortino_ratio | -0.7052 |
| max_drawdown | 0.5743 |
| cagr | -0.2825 |
| net_avg_win | 65.9841 |
| net_avg_loss | -83.3376 |
| avg_hold_time_bars | 26.8801 |
| exposure | 0.4179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
