# EMA Hourly Continuation — IOTX/USDT P8_144

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7100 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.6411 |
| sortino_ratio | -0.4015 |
| max_drawdown | 0.3892 |
| cagr | -0.1705 |
| net_avg_win | 61.5665 |
| net_avg_loss | -87.2995 |
| avg_hold_time_bars | 62.3367 |
| exposure | 0.8415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
