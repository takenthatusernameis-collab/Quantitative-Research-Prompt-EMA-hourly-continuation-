# EMA Hourly Continuation — ETN/USDT P8_200

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5735 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.6801 |
| gross_win_rate | 0.4106 |
| sharpe_ratio | -3.6548 |
| sortino_ratio | -1.1201 |
| max_drawdown | 0.6702 |
| cagr | -0.4042 |
| net_avg_win | 54.7158 |
| net_avg_loss | -66.4576 |
| avg_hold_time_bars | 29.9572 |
| exposure | 0.6460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
