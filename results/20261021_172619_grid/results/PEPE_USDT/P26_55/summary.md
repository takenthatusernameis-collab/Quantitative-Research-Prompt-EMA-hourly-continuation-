# EMA Hourly Continuation — PEPE/USDT P26_55

**Symbol:** PEPE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7920 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0194 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.4282 |
| sortino_ratio | -0.3954 |
| max_drawdown | 0.3784 |
| cagr | -0.1665 |
| net_avg_win | 74.3455 |
| net_avg_loss | -95.9076 |
| avg_hold_time_bars | 6.7527 |
| exposure | 0.1142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
