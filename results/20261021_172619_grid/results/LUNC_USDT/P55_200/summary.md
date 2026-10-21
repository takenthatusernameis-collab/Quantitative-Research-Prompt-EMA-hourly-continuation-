# EMA Hourly Continuation — LUNC/USDT P55_200

**Symbol:** LUNC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8899 |
| net_win_rate | 0.5359 |
| gross_profit_factor | 1.1414 |
| gross_win_rate | 0.5359 |
| sharpe_ratio | -0.5801 |
| sortino_ratio | -0.1466 |
| max_drawdown | 0.2106 |
| cagr | -0.0678 |
| net_avg_win | 79.6874 |
| net_avg_loss | -103.4202 |
| avg_hold_time_bars | 24.8399 |
| exposure | 0.3455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
