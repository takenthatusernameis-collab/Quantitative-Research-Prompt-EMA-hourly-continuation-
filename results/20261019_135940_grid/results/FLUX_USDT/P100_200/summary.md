# EMA Hourly Continuation — FLUX/USDT P100_200

**Symbol:** FLUX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7008 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0826 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -2.1589 |
| sortino_ratio | -0.6149 |
| max_drawdown | 0.5329 |
| cagr | -0.2502 |
| net_avg_win | 58.8177 |
| net_avg_loss | -88.2292 |
| avg_hold_time_bars | 9.0575 |
| exposure | 0.1647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
