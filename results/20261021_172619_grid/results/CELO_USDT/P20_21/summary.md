# EMA Hourly Continuation — CELO/USDT P20_21

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 212 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.8149 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -3.0087 |
| sortino_ratio | -0.6261 |
| max_drawdown | 0.5301 |
| cagr | -0.2519 |
| net_avg_win | 63.8721 |
| net_avg_loss | -93.5360 |
| avg_hold_time_bars | 4.0755 |
| exposure | 0.0391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
