# EMA Hourly Continuation — G/USDT P20_100

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.4880 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.7577 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -4.9090 |
| sortino_ratio | -1.6244 |
| max_drawdown | 0.8312 |
| cagr | -0.5371 |
| net_avg_win | 38.3272 |
| net_avg_loss | -57.8979 |
| avg_hold_time_bars | 20.7311 |
| exposure | 0.5189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
