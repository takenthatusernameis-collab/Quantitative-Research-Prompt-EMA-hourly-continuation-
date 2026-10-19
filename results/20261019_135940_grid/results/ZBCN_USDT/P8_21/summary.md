# EMA Hourly Continuation — ZBCN/USDT P8_21

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1806 |
| net_profit_factor | 0.3965 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.7390 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -10.2155 |
| sortino_ratio | -6.1583 |
| max_drawdown | 0.9995 |
| cagr | -0.9529 |
| net_avg_win | 8.1084 |
| net_avg_loss | -16.6290 |
| avg_hold_time_bars | 2.6213 |
| exposure | 0.2190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
