# EMA Hourly Continuation — XPR/USDT P50_144

**Symbol:** XPR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.4377 |
| net_win_rate | 0.4288 |
| gross_profit_factor | 0.7293 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -5.5550 |
| sortino_ratio | -1.8040 |
| max_drawdown | 0.8921 |
| cagr | -0.5867 |
| net_avg_win | 30.2956 |
| net_avg_loss | -51.9678 |
| avg_hold_time_bars | 9.6704 |
| exposure | 0.2347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
