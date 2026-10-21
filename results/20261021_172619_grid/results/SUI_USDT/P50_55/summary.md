# EMA Hourly Continuation — SUI/USDT P50_55

**Symbol:** SUI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 73 |
| net_profit_factor | 0.8470 |
| net_win_rate | 0.5342 |
| gross_profit_factor | 1.1372 |
| gross_win_rate | 0.5342 |
| sharpe_ratio | -0.4203 |
| sortino_ratio | -0.0520 |
| max_drawdown | 0.0913 |
| cagr | -0.0238 |
| net_avg_win | 83.3088 |
| net_avg_loss | -112.8261 |
| avg_hold_time_bars | 4.8904 |
| exposure | 0.0162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
