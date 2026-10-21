# EMA Hourly Continuation — PYTH/USDT P89_200

**Symbol:** PYTH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.8813 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0699 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.5557 |
| sortino_ratio | -0.1255 |
| max_drawdown | 0.2126 |
| cagr | -0.0583 |
| net_avg_win | 81.2058 |
| net_avg_loss | -99.9465 |
| avg_hold_time_bars | 15.2439 |
| exposure | 0.1705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
