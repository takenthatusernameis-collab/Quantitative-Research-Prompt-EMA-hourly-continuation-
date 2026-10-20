# EMA Hourly Continuation — RPL/USDT P8_50

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 1.0294 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -4.5130 |
| sortino_ratio | -1.9413 |
| max_drawdown | 0.9084 |
| cagr | -0.6051 |
| net_avg_win | 37.3085 |
| net_avg_loss | -52.5293 |
| avg_hold_time_bars | 11.6691 |
| exposure | 0.4964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
