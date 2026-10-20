# EMA Hourly Continuation — REZ/USDT P21_55

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.6576 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -4.6202 |
| sortino_ratio | -1.9775 |
| max_drawdown | 0.9123 |
| cagr | -0.6122 |
| net_avg_win | 39.3802 |
| net_avg_loss | -56.6678 |
| avg_hold_time_bars | 5.8986 |
| exposure | 0.2468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
