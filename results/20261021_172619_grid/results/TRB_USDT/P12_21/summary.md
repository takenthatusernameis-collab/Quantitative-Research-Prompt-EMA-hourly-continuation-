# EMA Hourly Continuation — TRB/USDT P12_21

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.5185 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.7306 |
| gross_win_rate | 0.4048 |
| sharpe_ratio | -4.1915 |
| sortino_ratio | -1.0838 |
| max_drawdown | 0.7316 |
| cagr | -0.3947 |
| net_avg_win | 57.7025 |
| net_avg_loss | -75.7021 |
| avg_hold_time_bars | 4.7976 |
| exposure | 0.0719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
