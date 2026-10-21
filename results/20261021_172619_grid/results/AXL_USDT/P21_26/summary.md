# EMA Hourly Continuation — AXL/USDT P21_26

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.3643 |
| gross_profit_factor | 0.6093 |
| gross_win_rate | 0.3643 |
| sharpe_ratio | -4.5307 |
| sortino_ratio | -1.0540 |
| max_drawdown | 0.7239 |
| cagr | -0.3898 |
| net_avg_win | 56.7511 |
| net_avg_loss | -74.1836 |
| avg_hold_time_bars | 5.0186 |
| exposure | 0.0611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
