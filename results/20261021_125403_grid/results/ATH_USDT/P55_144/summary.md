# EMA Hourly Continuation — ATH/USDT P55_144

**Symbol:** ATH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7741 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.4245 |
| sortino_ratio | -0.3722 |
| max_drawdown | 0.3576 |
| cagr | -0.1581 |
| net_avg_win | 74.6229 |
| net_avg_loss | -91.6154 |
| avg_hold_time_bars | 15.1306 |
| exposure | 0.2303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
