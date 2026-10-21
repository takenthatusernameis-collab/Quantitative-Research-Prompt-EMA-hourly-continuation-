# EMA Hourly Continuation — ANKR/USDT P20_200

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.8137 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 1.0283 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -1.1746 |
| sortino_ratio | -0.2907 |
| max_drawdown | 0.3599 |
| cagr | -0.1271 |
| net_avg_win | 83.6298 |
| net_avg_loss | -104.8607 |
| avg_hold_time_bars | 50.1505 |
| exposure | 0.6816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
