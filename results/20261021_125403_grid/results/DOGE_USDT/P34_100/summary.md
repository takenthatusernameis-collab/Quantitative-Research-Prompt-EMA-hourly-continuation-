# EMA Hourly Continuation — DOGE/USDT P34_100

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6162 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -2.6681 |
| sortino_ratio | -0.7348 |
| max_drawdown | 0.5788 |
| cagr | -0.2854 |
| net_avg_win | 52.8988 |
| net_avg_loss | -74.2575 |
| avg_hold_time_bars | 15.1984 |
| exposure | 0.2577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
