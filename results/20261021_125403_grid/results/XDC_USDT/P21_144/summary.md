# EMA Hourly Continuation — XDC/USDT P21_144

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.8087 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.1006 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -1.3125 |
| sortino_ratio | -0.3942 |
| max_drawdown | 0.3722 |
| cagr | -0.1662 |
| net_avg_win | 67.6332 |
| net_avg_loss | -92.5226 |
| avg_hold_time_bars | 21.2133 |
| exposure | 0.4204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
