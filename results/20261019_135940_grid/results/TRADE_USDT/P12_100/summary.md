# EMA Hourly Continuation — TRADE/USDT P12_100

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -3.4665 |
| sortino_ratio | -1.1656 |
| max_drawdown | 0.7803 |
| cagr | -0.4337 |
| net_avg_win | 52.8331 |
| net_avg_loss | -70.5956 |
| avg_hold_time_bars | 20.5450 |
| exposure | 0.5398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
