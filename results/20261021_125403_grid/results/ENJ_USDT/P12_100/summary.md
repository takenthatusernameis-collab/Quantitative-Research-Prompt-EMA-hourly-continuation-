# EMA Hourly Continuation — ENJ/USDT P12_100

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8382 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0340 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.3061 |
| sortino_ratio | -0.4020 |
| max_drawdown | 0.5059 |
| cagr | -0.1705 |
| net_avg_win | 83.1990 |
| net_avg_loss | -100.9898 |
| avg_hold_time_bars | 26.7651 |
| exposure | 0.5620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
