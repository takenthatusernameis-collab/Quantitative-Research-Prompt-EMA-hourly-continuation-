# EMA Hourly Continuation — POKT/USDT P89_100

**Symbol:** POKT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.4997 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7124 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -3.1415 |
| sortino_ratio | -0.6049 |
| max_drawdown | 0.5212 |
| cagr | -0.2455 |
| net_avg_win | 68.6476 |
| net_avg_loss | -91.5907 |
| avg_hold_time_bars | 6.8162 |
| exposure | 0.0571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
