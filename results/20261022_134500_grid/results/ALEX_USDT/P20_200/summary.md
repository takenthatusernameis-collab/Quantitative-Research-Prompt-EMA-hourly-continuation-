# EMA Hourly Continuation — ALEX/USDT P20_200

**Symbol:** ALEX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6124 |
| net_win_rate | 0.4359 |
| gross_profit_factor | 0.7960 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -2.8606 |
| sortino_ratio | -0.7095 |
| max_drawdown | 0.5939 |
| cagr | -0.2855 |
| net_avg_win | 66.2336 |
| net_avg_loss | -83.5770 |
| avg_hold_time_bars | 48.9135 |
| exposure | 0.6937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
