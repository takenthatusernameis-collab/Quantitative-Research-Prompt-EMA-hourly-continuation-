# EMA Hourly Continuation — SQD/USDT P34_100

**Symbol:** SQD/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -2.3204 |
| sortino_ratio | -0.6759 |
| max_drawdown | 0.5442 |
| cagr | -0.2678 |
| net_avg_win | 70.7220 |
| net_avg_loss | -83.1661 |
| avg_hold_time_bars | 12.8676 |
| exposure | 0.2468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
