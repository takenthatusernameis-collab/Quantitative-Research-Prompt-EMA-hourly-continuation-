# EMA Hourly Continuation — ORCA/USDT P12_89

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6550 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -3.1425 |
| sortino_ratio | -1.0969 |
| max_drawdown | 0.7627 |
| cagr | -0.4134 |
| net_avg_win | 45.6348 |
| net_avg_loss | -67.4773 |
| avg_hold_time_bars | 20.0337 |
| exposure | 0.5682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
