# EMA Hourly Continuation — CTC/USDT P12_100

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.8539 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.0967 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -1.0480 |
| sortino_ratio | -0.3434 |
| max_drawdown | 0.4187 |
| cagr | -0.1494 |
| net_avg_win | 71.4590 |
| net_avg_loss | -93.2538 |
| avg_hold_time_bars | 23.9903 |
| exposure | 0.5649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
