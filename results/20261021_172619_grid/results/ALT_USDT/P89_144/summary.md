# EMA Hourly Continuation — ALT/USDT P89_144

**Symbol:** ALT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.6532 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8630 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.2641 |
| sortino_ratio | -0.5589 |
| max_drawdown | 0.4851 |
| cagr | -0.2268 |
| net_avg_win | 63.9959 |
| net_avg_loss | -85.7321 |
| avg_hold_time_bars | 9.1400 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
