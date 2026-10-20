# EMA Hourly Continuation — RIO/USDT P55_200

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6116 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8242 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -3.5224 |
| sortino_ratio | -1.0984 |
| max_drawdown | 0.7617 |
| cagr | -0.4091 |
| net_avg_win | 52.0020 |
| net_avg_loss | -70.1101 |
| avg_hold_time_bars | 14.5215 |
| exposure | 0.3260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
