# EMA Hourly Continuation — APT/USDT P8_100

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7345 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0273 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -2.1393 |
| sortino_ratio | -0.6967 |
| max_drawdown | 0.5950 |
| cagr | -0.2818 |
| net_avg_win | 58.2833 |
| net_avg_loss | -81.4751 |
| avg_hold_time_bars | 29.6673 |
| exposure | 0.7134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
