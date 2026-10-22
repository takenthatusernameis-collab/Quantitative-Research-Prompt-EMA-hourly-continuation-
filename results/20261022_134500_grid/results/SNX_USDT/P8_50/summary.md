# EMA Hourly Continuation — SNX/USDT P8_50

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -5.3505 |
| sortino_ratio | -2.4805 |
| max_drawdown | 0.9520 |
| cagr | -0.6978 |
| net_avg_win | 29.6236 |
| net_avg_loss | -44.3351 |
| avg_hold_time_bars | 9.1413 |
| exposure | 0.4538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
