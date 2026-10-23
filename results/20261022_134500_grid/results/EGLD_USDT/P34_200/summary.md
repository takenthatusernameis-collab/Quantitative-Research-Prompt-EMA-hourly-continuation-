# EMA Hourly Continuation — EGLD/USDT P34_200

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0297 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.6657 |
| sortino_ratio | -0.4422 |
| max_drawdown | 0.4278 |
| cagr | -0.1880 |
| net_avg_win | 60.0465 |
| net_avg_loss | -85.8225 |
| avg_hold_time_bars | 32.4143 |
| exposure | 0.5157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
