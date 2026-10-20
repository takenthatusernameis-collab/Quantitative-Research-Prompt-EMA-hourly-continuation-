# EMA Hourly Continuation — KSM/USDT P8_100

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.6005 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.9057 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -4.4547 |
| sortino_ratio | -1.5585 |
| max_drawdown | 0.8485 |
| cagr | -0.5241 |
| net_avg_win | 45.2013 |
| net_avg_loss | -62.2132 |
| avg_hold_time_bars | 24.3398 |
| exposure | 0.6870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
