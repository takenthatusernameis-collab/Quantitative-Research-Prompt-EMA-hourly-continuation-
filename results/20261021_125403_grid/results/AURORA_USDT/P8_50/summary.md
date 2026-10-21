# EMA Hourly Continuation — AURORA/USDT P8_50

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -3.5055 |
| sortino_ratio | -1.2631 |
| max_drawdown | 0.7975 |
| cagr | -0.4418 |
| net_avg_win | 60.1395 |
| net_avg_loss | -75.0546 |
| avg_hold_time_bars | 14.9984 |
| exposure | 0.4370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
