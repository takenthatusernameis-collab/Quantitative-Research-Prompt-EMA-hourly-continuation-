# EMA Hourly Continuation — MANTA/USDT P50_144

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6699 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.6061 |
| sortino_ratio | -0.7799 |
| max_drawdown | 0.6107 |
| cagr | -0.3075 |
| net_avg_win | 56.3681 |
| net_avg_loss | -79.0399 |
| avg_hold_time_bars | 17.0960 |
| exposure | 0.3481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
