# EMA Hourly Continuation — COMP/USDT P20_21

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -2.5609 |
| sortino_ratio | -0.5218 |
| max_drawdown | 0.4566 |
| cagr | -0.2128 |
| net_avg_win | 59.7580 |
| net_avg_loss | -97.0905 |
| avg_hold_time_bars | 4.1300 |
| exposure | 0.0375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
