# EMA Hourly Continuation — IO/USDT P26_200

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.8353 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -0.9591 |
| sortino_ratio | -0.2404 |
| max_drawdown | 0.2617 |
| cagr | -0.1065 |
| net_avg_win | 83.2955 |
| net_avg_loss | -96.3311 |
| avg_hold_time_bars | 38.9343 |
| exposure | 0.5447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
