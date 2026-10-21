# EMA Hourly Continuation — TAO/USDT P8_26

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.8838 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.1172 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.9498 |
| sortino_ratio | -0.3277 |
| max_drawdown | 0.4287 |
| cagr | -0.1442 |
| net_avg_win | 81.5094 |
| net_avg_loss | -103.1552 |
| avg_hold_time_bars | 6.7465 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
