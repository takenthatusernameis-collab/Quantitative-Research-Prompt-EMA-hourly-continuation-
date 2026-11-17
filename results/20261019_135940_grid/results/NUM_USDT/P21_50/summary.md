# EMA Hourly Continuation — NUM/USDT P21_50

**Symbol:** NUM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.3550 |
| net_win_rate | 0.3450 |
| gross_profit_factor | 0.7294 |
| gross_win_rate | 0.3647 |
| sharpe_ratio | -10.9008 |
| sortino_ratio | -4.7954 |
| max_drawdown | 0.9977 |
| cagr | -0.9096 |
| net_avg_win | 16.4383 |
| net_avg_loss | -24.3951 |
| avg_hold_time_bars | 5.2355 |
| exposure | 0.2304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
