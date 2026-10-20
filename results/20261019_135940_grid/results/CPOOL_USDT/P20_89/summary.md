# EMA Hourly Continuation — CPOOL/USDT P20_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.6366 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8742 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -3.9291 |
| sortino_ratio | -1.5450 |
| max_drawdown | 0.8522 |
| cagr | -0.5230 |
| net_avg_win | 40.0786 |
| net_avg_loss | -55.9778 |
| avg_hold_time_bars | 9.6811 |
| exposure | 0.3450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
