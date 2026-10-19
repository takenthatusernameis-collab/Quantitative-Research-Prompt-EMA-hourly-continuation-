# EMA Hourly Continuation — JASMY/USDT P21_34

**Symbol:** JASMY/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.3562 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.7192 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -10.7310 |
| sortino_ratio | -5.1460 |
| max_drawdown | 0.9987 |
| cagr | -0.9280 |
| net_avg_win | 11.5858 |
| net_avg_loss | -23.3981 |
| avg_hold_time_bars | 2.1947 |
| exposure | 0.1137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
