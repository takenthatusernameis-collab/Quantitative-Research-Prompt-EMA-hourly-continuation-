# EMA Hourly Continuation — VELO/USDT P8_100

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.9191 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0730 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -0.5438 |
| sortino_ratio | -0.1823 |
| max_drawdown | 0.3494 |
| cagr | -0.0869 |
| net_avg_win | 81.9177 |
| net_avg_loss | -97.0138 |
| avg_hold_time_bars | 23.8103 |
| exposure | 0.5877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
