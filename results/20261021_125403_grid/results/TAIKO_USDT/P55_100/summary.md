# EMA Hourly Continuation — TAIKO/USDT P55_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6507 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.8972 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.3208 |
| sortino_ratio | -0.6146 |
| max_drawdown | 0.4893 |
| cagr | -0.2441 |
| net_avg_win | 58.0207 |
| net_avg_loss | -82.7926 |
| avg_hold_time_bars | 8.0586 |
| exposure | 0.1254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
