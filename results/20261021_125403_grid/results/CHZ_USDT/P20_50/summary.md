# EMA Hourly Continuation — CHZ/USDT P20_50

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9743 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -2.4999 |
| sortino_ratio | -0.8128 |
| max_drawdown | 0.6202 |
| cagr | -0.3107 |
| net_avg_win | 63.3944 |
| net_avg_loss | -82.9563 |
| avg_hold_time_bars | 8.0000 |
| exposure | 0.1876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
