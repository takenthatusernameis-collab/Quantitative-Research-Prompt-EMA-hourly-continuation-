# EMA Hourly Continuation — JUP/USDT P144_200

**Symbol:** JUP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.4514 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.7359 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -4.7599 |
| sortino_ratio | -1.3713 |
| max_drawdown | 0.8203 |
| cagr | -0.4880 |
| net_avg_win | 37.2079 |
| net_avg_loss | -62.8640 |
| avg_hold_time_bars | 4.0481 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
