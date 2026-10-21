# EMA Hourly Continuation — ORCA/USDT P8_20

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.7175 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0390 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -2.8493 |
| sortino_ratio | -1.0701 |
| max_drawdown | 0.7408 |
| cagr | -0.3888 |
| net_avg_win | 51.9457 |
| net_avg_loss | -74.3223 |
| avg_hold_time_bars | 5.7781 |
| exposure | 0.1799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
