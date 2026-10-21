# EMA Hourly Continuation — KAS/USDT P8_144

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.9413 |
| net_win_rate | 0.5358 |
| gross_profit_factor | 1.1376 |
| gross_win_rate | 0.5358 |
| sharpe_ratio | -0.3174 |
| sortino_ratio | -0.0921 |
| max_drawdown | 0.1754 |
| cagr | -0.0472 |
| net_avg_win | 84.5141 |
| net_avg_loss | -103.6373 |
| avg_hold_time_bars | 38.6864 |
| exposure | 0.7122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
