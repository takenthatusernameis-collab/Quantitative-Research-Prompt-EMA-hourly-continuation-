# EMA Hourly Continuation — AEVO/USDT P55_144

**Symbol:** AEVO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6869 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9796 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -2.6254 |
| sortino_ratio | -0.8461 |
| max_drawdown | 0.6422 |
| cagr | -0.3273 |
| net_avg_win | 53.9720 |
| net_avg_loss | -77.3648 |
| avg_hold_time_bars | 11.1467 |
| exposure | 0.2613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
