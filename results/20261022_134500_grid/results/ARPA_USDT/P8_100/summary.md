# EMA Hourly Continuation — ARPA/USDT P8_100

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 800 |
| net_profit_factor | 0.5455 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -5.6470 |
| sortino_ratio | -2.2352 |
| max_drawdown | 0.9373 |
| cagr | -0.6626 |
| net_avg_win | 31.3605 |
| net_avg_loss | -46.5650 |
| avg_hold_time_bars | 16.9862 |
| exposure | 0.6149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
