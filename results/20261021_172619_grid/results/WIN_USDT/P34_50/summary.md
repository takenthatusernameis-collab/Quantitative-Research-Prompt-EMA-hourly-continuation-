# EMA Hourly Continuation — WIN/USDT P34_50

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.6419 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0453 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -2.0283 |
| sortino_ratio | -0.4331 |
| max_drawdown | 0.4234 |
| cagr | -0.1786 |
| net_avg_win | 62.9685 |
| net_avg_loss | -101.7583 |
| avg_hold_time_bars | 5.3211 |
| exposure | 0.0527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
