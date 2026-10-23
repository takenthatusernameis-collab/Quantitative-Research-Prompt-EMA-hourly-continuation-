# EMA Hourly Continuation — OSMO/USDT P8_34

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1391 |
| net_profit_factor | 0.6048 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 1.1107 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -9.2987 |
| sortino_ratio | -4.8892 |
| max_drawdown | 0.9975 |
| cagr | -0.9080 |
| net_avg_win | 25.1455 |
| net_avg_loss | -32.1917 |
| avg_hold_time_bars | 5.7002 |
| exposure | 0.3604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
