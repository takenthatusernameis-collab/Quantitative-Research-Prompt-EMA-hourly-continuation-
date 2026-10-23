# EMA Hourly Continuation — SSV/USDT P21_100

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5674 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8303 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -4.9550 |
| sortino_ratio | -1.8499 |
| max_drawdown | 0.9027 |
| cagr | -0.5871 |
| net_avg_win | 37.1619 |
| net_avg_loss | -52.3662 |
| avg_hold_time_bars | 12.9351 |
| exposure | 0.4150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
