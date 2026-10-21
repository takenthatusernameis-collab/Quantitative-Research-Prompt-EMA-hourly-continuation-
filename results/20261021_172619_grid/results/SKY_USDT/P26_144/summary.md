# EMA Hourly Continuation — SKY/USDT P26_144

**Symbol:** SKY/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7658 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.6537 |
| sortino_ratio | -0.4674 |
| max_drawdown | 0.4498 |
| cagr | -0.1940 |
| net_avg_win | 74.3416 |
| net_avg_loss | -93.5027 |
| avg_hold_time_bars | 27.3875 |
| exposure | 0.4887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
