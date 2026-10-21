# EMA Hourly Continuation — TRAC/USDT P8_34

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.7175 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.0015 |
| sortino_ratio | -1.1125 |
| max_drawdown | 0.7413 |
| cagr | -0.4002 |
| net_avg_win | 57.3825 |
| net_avg_loss | -71.8874 |
| avg_hold_time_bars | 10.0385 |
| exposure | 0.3085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
