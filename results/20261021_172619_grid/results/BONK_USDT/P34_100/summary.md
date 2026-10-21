# EMA Hourly Continuation — BONK/USDT P34_100

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.8422 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.0175 |
| sortino_ratio | -0.2861 |
| max_drawdown | 0.3616 |
| cagr | -0.1253 |
| net_avg_win | 78.5930 |
| net_avg_loss | -94.7793 |
| avg_hold_time_bars | 13.8182 |
| exposure | 0.2418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
