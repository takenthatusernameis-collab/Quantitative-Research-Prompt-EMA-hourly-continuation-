# EMA Hourly Continuation — ZRX/USDT P50_100

**Symbol:** ZRX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6791 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -2.4998 |
| sortino_ratio | -0.7499 |
| max_drawdown | 0.5884 |
| cagr | -0.2899 |
| net_avg_win | 56.5083 |
| net_avg_loss | -80.5955 |
| avg_hold_time_bars | 8.4624 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
