# EMA Hourly Continuation — LINK/USDT P34_100

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7201 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -2.1893 |
| sortino_ratio | -0.6087 |
| max_drawdown | 0.5110 |
| cagr | -0.2437 |
| net_avg_win | 71.6737 |
| net_avg_loss | -90.9841 |
| avg_hold_time_bars | 14.1847 |
| exposure | 0.2444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
