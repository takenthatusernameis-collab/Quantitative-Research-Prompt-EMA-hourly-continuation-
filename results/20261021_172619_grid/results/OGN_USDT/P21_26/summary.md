# EMA Hourly Continuation — OGN/USDT P21_26

**Symbol:** OGN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.4965 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.7997 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -3.7703 |
| sortino_ratio | -0.8958 |
| max_drawdown | 0.6545 |
| cagr | -0.3407 |
| net_avg_win | 53.4382 |
| net_avg_loss | -83.3325 |
| avg_hold_time_bars | 5.4764 |
| exposure | 0.0681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
