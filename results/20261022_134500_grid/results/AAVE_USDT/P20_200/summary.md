# EMA Hourly Continuation — AAVE/USDT P20_200

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7661 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0906 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -1.4992 |
| sortino_ratio | -0.4108 |
| max_drawdown | 0.4835 |
| cagr | -0.1806 |
| net_avg_win | 64.7529 |
| net_avg_loss | -92.4231 |
| avg_hold_time_bars | 36.4383 |
| exposure | 0.6310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
