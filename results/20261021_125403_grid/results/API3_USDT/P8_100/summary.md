# EMA Hourly Continuation — API3/USDT P8_100

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7797 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -1.8384 |
| sortino_ratio | -0.6034 |
| max_drawdown | 0.5367 |
| cagr | -0.2427 |
| net_avg_win | 69.1867 |
| net_avg_loss | -83.8429 |
| avg_hold_time_bars | 26.5066 |
| exposure | 0.6374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
