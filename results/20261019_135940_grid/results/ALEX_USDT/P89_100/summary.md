# EMA Hourly Continuation — ALEX/USDT P89_100

**Symbol:** ALEX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.2338 |
| net_win_rate | 0.2885 |
| gross_profit_factor | 0.6397 |
| gross_win_rate | 0.3142 |
| sharpe_ratio | -10.3456 |
| sortino_ratio | -3.3839 |
| max_drawdown | 0.9886 |
| cagr | -0.8308 |
| net_avg_win | 20.6619 |
| net_avg_loss | -35.8367 |
| avg_hold_time_bars | 4.9921 |
| exposure | 0.1148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
