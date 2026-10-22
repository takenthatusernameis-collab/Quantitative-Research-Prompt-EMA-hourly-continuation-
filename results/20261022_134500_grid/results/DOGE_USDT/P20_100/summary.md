# EMA Hourly Continuation — DOGE/USDT P20_100

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.5231 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8751 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -5.2062 |
| sortino_ratio | -1.7733 |
| max_drawdown | 0.8935 |
| cagr | -0.5813 |
| net_avg_win | 36.7443 |
| net_avg_loss | -56.9242 |
| avg_hold_time_bars | 17.0557 |
| exposure | 0.4590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
