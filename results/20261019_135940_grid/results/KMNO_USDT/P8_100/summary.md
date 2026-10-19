# EMA Hourly Continuation — KMNO/USDT P8_100

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.7015 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.8935 |
| sortino_ratio | -0.9534 |
| max_drawdown | 0.6845 |
| cagr | -0.3692 |
| net_avg_win | 61.2162 |
| net_avg_loss | -79.6394 |
| avg_hold_time_bars | 26.4077 |
| exposure | 0.6669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
