# EMA Hourly Continuation — JASMY/USDT P20_34

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1143 |
| net_profit_factor | 0.3569 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.7007 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -10.5398 |
| sortino_ratio | -5.0501 |
| max_drawdown | 0.9985 |
| cagr | -0.9238 |
| net_avg_win | 11.5899 |
| net_avg_loss | -23.3450 |
| avg_hold_time_bars | 2.3613 |
| exposure | 0.1227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
