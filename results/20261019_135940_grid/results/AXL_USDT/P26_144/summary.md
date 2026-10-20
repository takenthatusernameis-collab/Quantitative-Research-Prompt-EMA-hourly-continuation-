# EMA Hourly Continuation — AXL/USDT P26_144

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.6551 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -3.8213 |
| sortino_ratio | -1.2980 |
| max_drawdown | 0.7949 |
| cagr | -0.4625 |
| net_avg_win | 56.2797 |
| net_avg_loss | -71.0158 |
| avg_hold_time_bars | 16.6932 |
| exposure | 0.4457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
