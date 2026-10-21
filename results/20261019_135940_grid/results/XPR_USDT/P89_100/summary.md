# EMA Hourly Continuation — XPR/USDT P89_100

**Symbol:** XPR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.1785 |
| net_win_rate | 0.2955 |
| gross_profit_factor | 0.5673 |
| gross_win_rate | 0.3392 |
| sharpe_ratio | -12.0017 |
| sortino_ratio | -4.3713 |
| max_drawdown | 0.9978 |
| cagr | -0.9118 |
| net_avg_win | 12.8314 |
| net_avg_loss | -30.1391 |
| avg_hold_time_bars | 2.3934 |
| exposure | 0.0622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
