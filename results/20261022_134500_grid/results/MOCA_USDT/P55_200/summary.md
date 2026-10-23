# EMA Hourly Continuation — MOCA/USDT P55_200

**Symbol:** MOCA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6053 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9386 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -3.0034 |
| sortino_ratio | -0.8252 |
| max_drawdown | 0.6209 |
| cagr | -0.3303 |
| net_avg_win | 54.0000 |
| net_avg_loss | -85.2061 |
| avg_hold_time_bars | 22.0546 |
| exposure | 0.3848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
