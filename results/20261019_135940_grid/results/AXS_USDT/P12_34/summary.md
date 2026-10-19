# EMA Hourly Continuation — AXS/USDT P12_34

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1236 |
| net_profit_factor | 0.4477 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -8.1448 |
| sortino_ratio | -4.0312 |
| max_drawdown | 0.9934 |
| cagr | -0.8634 |
| net_avg_win | 13.9100 |
| net_avg_loss | -27.3789 |
| avg_hold_time_bars | 4.0210 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
