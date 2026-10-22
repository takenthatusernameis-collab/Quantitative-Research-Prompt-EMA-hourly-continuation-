# EMA Hourly Continuation — ELON/USDT P89_100

**Symbol:** ELON/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 100 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9860 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0590 |
| sortino_ratio | -0.1520 |
| max_drawdown | 0.1678 |
| cagr | -0.0673 |
| net_avg_win | 75.7668 |
| net_avg_loss | -107.8807 |
| avg_hold_time_bars | 7.0100 |
| exposure | 0.0319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
