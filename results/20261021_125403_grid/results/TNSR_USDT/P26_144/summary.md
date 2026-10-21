# EMA Hourly Continuation — TNSR/USDT P26_144

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7471 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.8982 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -1.9124 |
| sortino_ratio | -0.5481 |
| max_drawdown | 0.4978 |
| cagr | -0.2243 |
| net_avg_win | 72.3993 |
| net_avg_loss | -86.9913 |
| avg_hold_time_bars | 25.3505 |
| exposure | 0.4681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
