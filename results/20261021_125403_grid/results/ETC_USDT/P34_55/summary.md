# EMA Hourly Continuation — ETC/USDT P34_55

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.5784 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -3.0125 |
| sortino_ratio | -0.7662 |
| max_drawdown | 0.5916 |
| cagr | -0.2956 |
| net_avg_win | 53.5277 |
| net_avg_loss | -85.1580 |
| avg_hold_time_bars | 5.1725 |
| exposure | 0.0736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
