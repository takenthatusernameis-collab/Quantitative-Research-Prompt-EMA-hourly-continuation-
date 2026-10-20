# EMA Hourly Continuation — SSV/USDT P26_200

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6930 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.2046 |
| sortino_ratio | -0.6011 |
| max_drawdown | 0.5319 |
| cagr | -0.2442 |
| net_avg_win | 63.8781 |
| net_avg_loss | -85.9370 |
| avg_hold_time_bars | 36.0216 |
| exposure | 0.6047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
