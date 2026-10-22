# EMA Hourly Continuation — POKT/USDT P12_100

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6391 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.7852 |
| gross_win_rate | 0.4187 |
| sharpe_ratio | -3.8414 |
| sortino_ratio | -1.2479 |
| max_drawdown | 0.7736 |
| cagr | -0.4396 |
| net_avg_win | 60.7189 |
| net_avg_loss | -68.4260 |
| avg_hold_time_bars | 22.5290 |
| exposure | 0.5454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
