# EMA Hourly Continuation — SHIB/USDT P8_21

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.7481 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0748 |
| gross_win_rate | 0.5182 |
| sharpe_ratio | -2.0143 |
| sortino_ratio | -0.6279 |
| max_drawdown | 0.5379 |
| cagr | -0.2492 |
| net_avg_win | 62.9843 |
| net_avg_loss | -90.5492 |
| avg_hold_time_bars | 5.5353 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
