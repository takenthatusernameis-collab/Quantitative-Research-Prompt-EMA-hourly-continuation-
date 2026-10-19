# EMA Hourly Continuation — ENA/USDT P89_200

**Symbol:** ENA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7178 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -2.0718 |
| sortino_ratio | -0.5611 |
| max_drawdown | 0.5323 |
| cagr | -0.2302 |
| net_avg_win | 69.2162 |
| net_avg_loss | -91.7592 |
| avg_hold_time_bars | 10.1267 |
| exposure | 0.1671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
