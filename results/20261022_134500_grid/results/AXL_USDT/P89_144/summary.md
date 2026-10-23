# EMA Hourly Continuation — AXL/USDT P89_144

**Symbol:** AXL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.5768 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8776 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -4.6047 |
| sortino_ratio | -1.5560 |
| max_drawdown | 0.8519 |
| cagr | -0.5185 |
| net_avg_win | 44.6404 |
| net_avg_loss | -63.7500 |
| avg_hold_time_bars | 5.4130 |
| exposure | 0.1394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
