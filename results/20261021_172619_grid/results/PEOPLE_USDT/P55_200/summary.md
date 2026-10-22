# EMA Hourly Continuation — PEOPLE/USDT P55_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8651 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0292 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -0.7285 |
| sortino_ratio | -0.1835 |
| max_drawdown | 0.3146 |
| cagr | -0.0834 |
| net_avg_win | 79.5529 |
| net_avg_loss | -96.8300 |
| avg_hold_time_bars | 25.9935 |
| exposure | 0.3646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
