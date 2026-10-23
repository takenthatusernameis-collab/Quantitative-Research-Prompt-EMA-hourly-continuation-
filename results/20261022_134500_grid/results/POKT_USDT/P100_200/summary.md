# EMA Hourly Continuation — POKT/USDT P100_200

**Symbol:** POKT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.4828 |
| net_win_rate | 0.3931 |
| gross_profit_factor | 0.7382 |
| gross_win_rate | 0.4017 |
| sharpe_ratio | -5.3281 |
| sortino_ratio | -1.6149 |
| max_drawdown | 0.8588 |
| cagr | -0.5365 |
| net_avg_win | 43.9237 |
| net_avg_loss | -58.9206 |
| avg_hold_time_bars | 10.5421 |
| exposure | 0.2209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
