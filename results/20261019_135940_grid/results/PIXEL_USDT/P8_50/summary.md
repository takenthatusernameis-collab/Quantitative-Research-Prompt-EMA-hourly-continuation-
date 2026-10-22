# EMA Hourly Continuation — PIXEL/USDT P8_50

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.6691 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -4.7061 |
| sortino_ratio | -2.1643 |
| max_drawdown | 0.9325 |
| cagr | -0.6444 |
| net_avg_win | 36.3025 |
| net_avg_loss | -50.0812 |
| avg_hold_time_bars | 9.8158 |
| exposure | 0.4775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
