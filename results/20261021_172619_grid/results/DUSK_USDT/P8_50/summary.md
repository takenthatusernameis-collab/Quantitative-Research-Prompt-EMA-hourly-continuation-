# EMA Hourly Continuation — DUSK/USDT P8_50

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.7907 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -2.6043 |
| sortino_ratio | -0.9979 |
| max_drawdown | 0.7564 |
| cagr | -0.3691 |
| net_avg_win | 75.5021 |
| net_avg_loss | -85.7399 |
| avg_hold_time_bars | 13.9159 |
| exposure | 0.4586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
