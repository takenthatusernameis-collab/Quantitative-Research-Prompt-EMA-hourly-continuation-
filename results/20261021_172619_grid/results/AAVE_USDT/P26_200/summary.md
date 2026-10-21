# EMA Hourly Continuation — AAVE/USDT P26_200

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.9429 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1176 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -0.2638 |
| sortino_ratio | -0.0648 |
| max_drawdown | 0.2418 |
| cagr | -0.0334 |
| net_avg_win | 87.6688 |
| net_avg_loss | -105.2867 |
| avg_hold_time_bars | 42.6621 |
| exposure | 0.5624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
