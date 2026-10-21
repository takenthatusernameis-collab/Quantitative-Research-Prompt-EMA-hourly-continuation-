# EMA Hourly Continuation — SAFE/USDT P34_200

**Symbol:** SAFE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.9992 |
| net_win_rate | 0.5483 |
| gross_profit_factor | 1.1969 |
| gross_win_rate | 0.5483 |
| sharpe_ratio | 0.0494 |
| sortino_ratio | 0.0122 |
| max_drawdown | 0.1232 |
| cagr | -0.0005 |
| net_avg_win | 92.4706 |
| net_avg_loss | -112.3275 |
| avg_hold_time_bars | 41.1448 |
| exposure | 0.5464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
