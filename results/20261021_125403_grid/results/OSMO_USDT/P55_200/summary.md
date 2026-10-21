# EMA Hourly Continuation — OSMO/USDT P55_200

**Symbol:** OSMO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7474 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -1.4838 |
| sortino_ratio | -0.3619 |
| max_drawdown | 0.3760 |
| cagr | -0.1539 |
| net_avg_win | 71.4207 |
| net_avg_loss | -90.4613 |
| avg_hold_time_bars | 25.9452 |
| exposure | 0.3444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
