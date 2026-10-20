# EMA Hourly Continuation — AGLD/USDT P8_55

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.6256 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9688 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -4.5708 |
| sortino_ratio | -1.9961 |
| max_drawdown | 0.9159 |
| cagr | -0.6131 |
| net_avg_win | 32.9476 |
| net_avg_loss | -47.9784 |
| avg_hold_time_bars | 11.2048 |
| exposure | 0.4903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
