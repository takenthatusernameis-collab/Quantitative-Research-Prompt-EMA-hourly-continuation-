# EMA Hourly Continuation — POKT/USDT P50_200

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5210 |
| net_win_rate | 0.4037 |
| gross_profit_factor | 0.7550 |
| gross_win_rate | 0.4119 |
| sharpe_ratio | -4.9429 |
| sortino_ratio | -1.5303 |
| max_drawdown | 0.8454 |
| cagr | -0.5202 |
| net_avg_win | 46.5451 |
| net_avg_loss | -60.4841 |
| avg_hold_time_bars | 19.6988 |
| exposure | 0.4350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
