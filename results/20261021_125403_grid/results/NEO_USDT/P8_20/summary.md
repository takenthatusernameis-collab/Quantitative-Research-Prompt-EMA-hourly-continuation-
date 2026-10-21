# EMA Hourly Continuation — NEO/USDT P8_20

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.6916 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0403 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -2.6541 |
| sortino_ratio | -0.9052 |
| max_drawdown | 0.6600 |
| cagr | -0.3368 |
| net_avg_win | 50.0998 |
| net_avg_loss | -76.9883 |
| avg_hold_time_bars | 5.5814 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
