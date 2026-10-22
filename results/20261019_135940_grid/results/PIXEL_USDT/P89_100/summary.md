# EMA Hourly Continuation — PIXEL/USDT P89_100

**Symbol:** PIXEL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.3816 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8891 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -7.6043 |
| sortino_ratio | -2.5784 |
| max_drawdown | 0.9638 |
| cagr | -0.7305 |
| net_avg_win | 24.8684 |
| net_avg_loss | -47.2042 |
| avg_hold_time_bars | 2.3480 |
| exposure | 0.0605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
