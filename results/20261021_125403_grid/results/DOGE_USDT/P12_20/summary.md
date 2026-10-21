# EMA Hourly Continuation — DOGE/USDT P12_20

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.6436 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -1.9288 |
| sortino_ratio | -0.4195 |
| max_drawdown | 0.4046 |
| cagr | -0.1750 |
| net_avg_win | 61.7853 |
| net_avg_loss | -91.1187 |
| avg_hold_time_bars | 4.6913 |
| exposure | 0.0490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
