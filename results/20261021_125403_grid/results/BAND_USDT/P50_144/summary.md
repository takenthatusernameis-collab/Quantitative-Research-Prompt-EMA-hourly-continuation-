# EMA Hourly Continuation — BAND/USDT P50_144

**Symbol:** BAND/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6008 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.7840 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -3.1124 |
| sortino_ratio | -0.8409 |
| max_drawdown | 0.6309 |
| cagr | -0.3220 |
| net_avg_win | 58.7651 |
| net_avg_loss | -76.3425 |
| avg_hold_time_bars | 17.8411 |
| exposure | 0.2947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
