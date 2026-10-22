# EMA Hourly Continuation — DAG/USDT P50_200

**Symbol:** DAG/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.9313 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0794 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.3158 |
| sortino_ratio | -0.0754 |
| max_drawdown | 0.1264 |
| cagr | -0.0377 |
| net_avg_win | 87.1098 |
| net_avg_loss | -101.3308 |
| avg_hold_time_bars | 26.4982 |
| exposure | 0.3312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
