# EMA Hourly Continuation — CARV/USDT P89_200

**Symbol:** CARV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.6579 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -1.9785 |
| sortino_ratio | -0.4491 |
| max_drawdown | 0.3624 |
| cagr | -0.1860 |
| net_avg_win | 69.0978 |
| net_avg_loss | -89.8835 |
| avg_hold_time_bars | 18.4903 |
| exposure | 0.2144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
