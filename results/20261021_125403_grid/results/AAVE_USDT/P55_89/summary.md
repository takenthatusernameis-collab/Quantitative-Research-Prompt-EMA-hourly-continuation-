# EMA Hourly Continuation — AAVE/USDT P55_89

**Symbol:** AAVE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8963 |
| net_win_rate | 0.5474 |
| gross_profit_factor | 1.2010 |
| gross_win_rate | 0.5474 |
| sharpe_ratio | -0.5471 |
| sortino_ratio | -0.1340 |
| max_drawdown | 0.2523 |
| cagr | -0.0620 |
| net_avg_win | 82.2782 |
| net_avg_loss | -111.0111 |
| avg_hold_time_bars | 6.5228 |
| exposure | 0.0845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
