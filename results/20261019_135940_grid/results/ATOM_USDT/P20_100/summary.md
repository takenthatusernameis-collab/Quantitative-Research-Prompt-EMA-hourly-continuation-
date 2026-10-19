# EMA Hourly Continuation — ATOM/USDT P20_100

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -3.7911 |
| sortino_ratio | -1.3405 |
| max_drawdown | 0.8150 |
| cagr | -0.4753 |
| net_avg_win | 37.0264 |
| net_avg_loss | -60.8591 |
| avg_hold_time_bars | 14.5665 |
| exposure | 0.4185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
