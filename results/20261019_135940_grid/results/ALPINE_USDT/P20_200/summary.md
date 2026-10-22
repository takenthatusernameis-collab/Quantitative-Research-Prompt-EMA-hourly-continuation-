# EMA Hourly Continuation — ALPINE/USDT P20_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.8575 |
| net_win_rate | 0.5307 |
| gross_profit_factor | 1.1154 |
| gross_win_rate | 0.5307 |
| sharpe_ratio | -0.6653 |
| sortino_ratio | -0.1436 |
| max_drawdown | 0.1949 |
| cagr | -0.0660 |
| net_avg_win | 78.3447 |
| net_avg_loss | -103.3237 |
| avg_hold_time_bars | 76.1667 |
| exposure | 0.7894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
