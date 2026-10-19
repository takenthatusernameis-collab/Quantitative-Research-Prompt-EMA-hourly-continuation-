# EMA Hourly Continuation — ZEC/USDT P26_100

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6874 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0657 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -3.0127 |
| sortino_ratio | -1.0600 |
| max_drawdown | 0.7316 |
| cagr | -0.3985 |
| net_avg_win | 50.8266 |
| net_avg_loss | -73.9371 |
| avg_hold_time_bars | 12.1266 |
| exposure | 0.3440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
