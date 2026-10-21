# EMA Hourly Continuation — POPCAT/USDT P20_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8604 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -0.8562 |
| sortino_ratio | -0.2187 |
| max_drawdown | 0.2904 |
| cagr | -0.0981 |
| net_avg_win | 90.6336 |
| net_avg_loss | -103.0693 |
| avg_hold_time_bars | 43.9782 |
| exposure | 0.6389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
