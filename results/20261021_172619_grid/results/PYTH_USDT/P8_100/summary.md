# EMA Hourly Continuation — PYTH/USDT P8_100

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.9422 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.0939 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -0.3595 |
| sortino_ratio | -0.1091 |
| max_drawdown | 0.3023 |
| cagr | -0.0550 |
| net_avg_win | 92.6962 |
| net_avg_loss | -108.6405 |
| avg_hold_time_bars | 33.6599 |
| exposure | 0.6793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
