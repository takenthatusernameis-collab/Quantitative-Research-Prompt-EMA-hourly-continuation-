# EMA Hourly Continuation — LISTA/USDT P21_200

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7749 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -1.5055 |
| sortino_ratio | -0.4096 |
| max_drawdown | 0.3753 |
| cagr | -0.1729 |
| net_avg_win | 75.6376 |
| net_avg_loss | -89.8836 |
| avg_hold_time_bars | 33.5059 |
| exposure | 0.5570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
