# EMA Hourly Continuation — JASMY/USDT P144_200

**Symbol:** JASMY/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.4912 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -4.0643 |
| sortino_ratio | -1.1343 |
| max_drawdown | 0.7527 |
| cagr | -0.4267 |
| net_avg_win | 39.0673 |
| net_avg_loss | -72.5191 |
| avg_hold_time_bars | 3.9872 |
| exposure | 0.0707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
