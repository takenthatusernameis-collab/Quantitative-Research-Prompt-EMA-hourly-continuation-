# EMA Hourly Continuation — TRAC/USDT P144_200

**Symbol:** TRAC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.7322 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9710 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.3722 |
| sortino_ratio | -0.2888 |
| max_drawdown | 0.2986 |
| cagr | -0.1238 |
| net_avg_win | 72.1870 |
| net_avg_loss | -96.7792 |
| avg_hold_time_bars | 8.3287 |
| exposure | 0.0818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
