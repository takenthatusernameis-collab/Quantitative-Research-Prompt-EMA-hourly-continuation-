# EMA Hourly Continuation — JUP/USDT P20_50

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.5752 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9514 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -5.5435 |
| sortino_ratio | -2.4499 |
| max_drawdown | 0.9472 |
| cagr | -0.6880 |
| net_avg_win | 27.4948 |
| net_avg_loss | -43.8503 |
| avg_hold_time_bars | 4.7197 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
