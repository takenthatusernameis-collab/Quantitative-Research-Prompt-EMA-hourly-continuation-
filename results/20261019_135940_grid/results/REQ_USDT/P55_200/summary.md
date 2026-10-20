# EMA Hourly Continuation — REQ/USDT P55_200

**Symbol:** REQ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.4386 |
| net_win_rate | 0.3828 |
| gross_profit_factor | 0.8287 |
| gross_win_rate | 0.4048 |
| sharpe_ratio | -7.1780 |
| sortino_ratio | -2.3784 |
| max_drawdown | 0.9503 |
| cagr | -0.6923 |
| net_avg_win | 35.4435 |
| net_avg_loss | -50.1171 |
| avg_hold_time_bars | 13.0275 |
| exposure | 0.3233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
