# EMA Hourly Continuation — ZBCN/USDT P55_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.6302 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9395 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -3.2540 |
| sortino_ratio | -1.0929 |
| max_drawdown | 0.7546 |
| cagr | -0.4147 |
| net_avg_win | 44.7916 |
| net_avg_loss | -67.9079 |
| avg_hold_time_bars | 7.4238 |
| exposure | 0.1961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
