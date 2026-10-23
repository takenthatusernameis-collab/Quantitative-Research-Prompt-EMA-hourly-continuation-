# EMA Hourly Continuation — BLZ/USDT P20_89

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.5780 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8805 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -5.9473 |
| sortino_ratio | -2.3336 |
| max_drawdown | 0.9441 |
| cagr | -0.6747 |
| net_avg_win | 38.0252 |
| net_avg_loss | -50.1165 |
| avg_hold_time_bars | 11.3929 |
| exposure | 0.4042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
