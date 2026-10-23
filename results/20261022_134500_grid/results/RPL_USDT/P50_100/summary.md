# EMA Hourly Continuation — RPL/USDT P50_100

**Symbol:** RPL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.5897 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.9043 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -4.0340 |
| sortino_ratio | -1.3769 |
| max_drawdown | 0.8041 |
| cagr | -0.4745 |
| net_avg_win | 42.4109 |
| net_avg_loss | -63.1034 |
| avg_hold_time_bars | 8.1340 |
| exposure | 0.2142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
