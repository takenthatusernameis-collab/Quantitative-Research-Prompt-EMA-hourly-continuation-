# EMA Hourly Continuation — TRADE/USDT P26_200

**Symbol:** TRADE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6359 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -2.6465 |
| sortino_ratio | -0.7002 |
| max_drawdown | 0.5882 |
| cagr | -0.2778 |
| net_avg_win | 62.9299 |
| net_avg_loss | -78.2577 |
| avg_hold_time_bars | 32.6809 |
| exposure | 0.5214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
