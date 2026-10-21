# EMA Hourly Continuation — CFG/USDT P8_100

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8253 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -2.2828 |
| sortino_ratio | -0.6716 |
| max_drawdown | 0.5720 |
| cagr | -0.2665 |
| net_avg_win | 65.5415 |
| net_avg_loss | -76.7489 |
| avg_hold_time_bars | 34.5301 |
| exposure | 0.6780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
