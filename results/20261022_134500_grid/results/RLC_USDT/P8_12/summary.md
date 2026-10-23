# EMA Hourly Continuation — RLC/USDT P8_12

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1728 |
| net_profit_factor | 0.2936 |
| net_win_rate | 0.4005 |
| gross_profit_factor | 0.8922 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -15.3783 |
| sortino_ratio | -9.1640 |
| max_drawdown | 1.0000 |
| cagr | -0.9915 |
| net_avg_win | 6.0057 |
| net_avg_loss | -13.6640 |
| avg_hold_time_bars | 2.2616 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
