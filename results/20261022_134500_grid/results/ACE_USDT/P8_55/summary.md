# EMA Hourly Continuation — ACE/USDT P8_55

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9585 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -3.6959 |
| sortino_ratio | -1.4399 |
| max_drawdown | 0.8223 |
| cagr | -0.4931 |
| net_avg_win | 45.4064 |
| net_avg_loss | -62.6960 |
| avg_hold_time_bars | 14.7914 |
| exposure | 0.5134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
