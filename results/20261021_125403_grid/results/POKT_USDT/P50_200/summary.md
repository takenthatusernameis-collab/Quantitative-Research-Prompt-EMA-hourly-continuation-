# EMA Hourly Continuation — POKT/USDT P50_200

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6853 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8392 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -2.3957 |
| sortino_ratio | -0.6209 |
| max_drawdown | 0.5497 |
| cagr | -0.2492 |
| net_avg_win | 74.2288 |
| net_avg_loss | -87.9312 |
| avg_hold_time_bars | 27.6291 |
| exposure | 0.4214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
