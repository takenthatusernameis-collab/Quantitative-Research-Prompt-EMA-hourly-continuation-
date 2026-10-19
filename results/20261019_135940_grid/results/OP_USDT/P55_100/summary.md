# EMA Hourly Continuation — OP/USDT P55_100

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5033 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -4.9995 |
| sortino_ratio | -1.7952 |
| max_drawdown | 0.8872 |
| cagr | -0.5763 |
| net_avg_win | 30.0723 |
| net_avg_loss | -51.4580 |
| avg_hold_time_bars | 4.7220 |
| exposure | 0.1382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
