# EMA Hourly Continuation — VET/USDT P20_100

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.5127 |
| gross_profit_factor | 1.1136 |
| gross_win_rate | 0.5232 |
| sharpe_ratio | -3.3711 |
| sortino_ratio | -1.2232 |
| max_drawdown | 0.7952 |
| cagr | -0.4477 |
| net_avg_win | 51.5994 |
| net_avg_loss | -78.0581 |
| avg_hold_time_bars | 13.9567 |
| exposure | 0.4244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
