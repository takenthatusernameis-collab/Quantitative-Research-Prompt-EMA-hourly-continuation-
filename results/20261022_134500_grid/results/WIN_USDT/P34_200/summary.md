# EMA Hourly Continuation — WIN/USDT P34_200

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5145 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8222 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.4315 |
| sortino_ratio | -0.9096 |
| max_drawdown | 0.6878 |
| cagr | -0.3508 |
| net_avg_win | 44.1341 |
| net_avg_loss | -70.3021 |
| avg_hold_time_bars | 30.9292 |
| exposure | 0.4963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
