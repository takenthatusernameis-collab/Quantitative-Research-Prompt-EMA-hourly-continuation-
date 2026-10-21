# EMA Hourly Continuation — LINK/USDT P20_144

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8697 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0803 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.7593 |
| sortino_ratio | -0.2003 |
| max_drawdown | 0.2981 |
| cagr | -0.0900 |
| net_avg_win | 80.4501 |
| net_avg_loss | -100.5428 |
| avg_hold_time_bars | 35.0357 |
| exposure | 0.5351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
