# EMA Hourly Continuation — RENDER/USDT P8_21

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8458 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1182 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | -1.1920 |
| sortino_ratio | -0.3893 |
| max_drawdown | 0.3807 |
| cagr | -0.1655 |
| net_avg_win | 76.2741 |
| net_avg_loss | -101.0135 |
| avg_hold_time_bars | 5.6372 |
| exposure | 0.1312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
