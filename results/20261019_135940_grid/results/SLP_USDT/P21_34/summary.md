# EMA Hourly Continuation — SLP/USDT P21_34

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1294 |
| net_profit_factor | 0.4033 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.9093 |
| gross_win_rate | 0.4235 |
| sharpe_ratio | -12.2686 |
| sortino_ratio | -6.3027 |
| max_drawdown | 0.9997 |
| cagr | -0.9595 |
| net_avg_win | 13.2218 |
| net_avg_loss | -21.3961 |
| avg_hold_time_bars | 2.5549 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
