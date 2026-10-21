# EMA Hourly Continuation — DGB/USDT P50_55

**Symbol:** DGB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 119 |
| net_profit_factor | 0.6096 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8538 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -1.6571 |
| sortino_ratio | -0.2584 |
| max_drawdown | 0.2761 |
| cagr | -0.1118 |
| net_avg_win | 73.1182 |
| net_avg_loss | -103.0758 |
| avg_hold_time_bars | 5.1681 |
| exposure | 0.0280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
