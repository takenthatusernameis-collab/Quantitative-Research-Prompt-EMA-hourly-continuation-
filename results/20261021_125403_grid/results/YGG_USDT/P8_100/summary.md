# EMA Hourly Continuation — YGG/USDT P8_100

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.9186 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0882 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -0.6427 |
| sortino_ratio | -0.2032 |
| max_drawdown | 0.4217 |
| cagr | -0.0941 |
| net_avg_win | 98.7893 |
| net_avg_loss | -116.3148 |
| avg_hold_time_bars | 30.5443 |
| exposure | 0.6703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
