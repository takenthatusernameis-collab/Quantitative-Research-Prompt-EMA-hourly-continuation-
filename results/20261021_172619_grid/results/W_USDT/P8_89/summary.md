# EMA Hourly Continuation — W/USDT P8_89

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.9612 |
| net_win_rate | 0.5335 |
| gross_profit_factor | 1.1301 |
| gross_win_rate | 0.5335 |
| sharpe_ratio | -0.1950 |
| sortino_ratio | -0.0616 |
| max_drawdown | 0.1921 |
| cagr | -0.0358 |
| net_avg_win | 84.9849 |
| net_avg_loss | -101.1006 |
| avg_hold_time_bars | 29.6904 |
| exposure | 0.6451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
