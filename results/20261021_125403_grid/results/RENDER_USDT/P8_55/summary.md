# EMA Hourly Continuation — RENDER/USDT P8_55

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.8429 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0355 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -1.2545 |
| sortino_ratio | -0.4806 |
| max_drawdown | 0.4427 |
| cagr | -0.2024 |
| net_avg_win | 65.6552 |
| net_avg_loss | -82.8796 |
| avg_hold_time_bars | 12.8483 |
| exposure | 0.4157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
