# EMA Hourly Continuation — RPL/USDT P50_89

**Symbol:** RPL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -3.1049 |
| sortino_ratio | -0.9276 |
| max_drawdown | 0.6632 |
| cagr | -0.3459 |
| net_avg_win | 60.1540 |
| net_avg_loss | -77.4419 |
| avg_hold_time_bars | 8.5769 |
| exposure | 0.1716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
