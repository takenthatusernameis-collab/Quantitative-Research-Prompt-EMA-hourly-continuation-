# EMA Hourly Continuation — ANKR/USDT P55_100

**Symbol:** ANKR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.4059 |
| net_win_rate | 0.4054 |
| gross_profit_factor | 0.7494 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -7.3841 |
| sortino_ratio | -2.6211 |
| max_drawdown | 0.9619 |
| cagr | -0.7269 |
| net_avg_win | 25.7666 |
| net_avg_loss | -43.2789 |
| avg_hold_time_bars | 7.3514 |
| exposure | 0.2102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
