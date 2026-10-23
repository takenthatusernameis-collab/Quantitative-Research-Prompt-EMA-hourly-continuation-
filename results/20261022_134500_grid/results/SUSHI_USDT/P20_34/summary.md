# EMA Hourly Continuation — SUSHI/USDT P20_34

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.4166 |
| net_win_rate | 0.4276 |
| gross_profit_factor | 0.9055 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -10.1185 |
| sortino_ratio | -4.9315 |
| max_drawdown | 0.9981 |
| cagr | -0.9158 |
| net_avg_win | 14.0323 |
| net_avg_loss | -25.1602 |
| avg_hold_time_bars | 2.6077 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
