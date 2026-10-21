# EMA Hourly Continuation — CVX/USDT P50_200

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8076 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.1233 |
| sortino_ratio | -0.2708 |
| max_drawdown | 0.2854 |
| cagr | -0.1185 |
| net_avg_win | 81.3890 |
| net_avg_loss | -97.3014 |
| avg_hold_time_bars | 29.0737 |
| exposure | 0.3766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
