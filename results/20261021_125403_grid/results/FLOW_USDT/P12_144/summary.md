# EMA Hourly Continuation — FLOW/USDT P12_144

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8529 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -0.9152 |
| sortino_ratio | -0.2472 |
| max_drawdown | 0.3219 |
| cagr | -0.1100 |
| net_avg_win | 81.3106 |
| net_avg_loss | -98.6018 |
| avg_hold_time_bars | 41.0309 |
| exposure | 0.6640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
