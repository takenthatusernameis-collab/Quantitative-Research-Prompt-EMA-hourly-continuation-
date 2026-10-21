# EMA Hourly Continuation — ROSE/USDT P8_12

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.7284 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9953 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5724 |
| sortino_ratio | -0.3587 |
| max_drawdown | 0.3666 |
| cagr | -0.1517 |
| net_avg_win | 72.0211 |
| net_avg_loss | -98.8771 |
| avg_hold_time_bars | 3.9127 |
| exposure | 0.0448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
