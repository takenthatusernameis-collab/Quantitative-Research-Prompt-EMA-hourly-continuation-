# EMA Hourly Continuation — ENA/USDT P55_144

**Symbol:** ENA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.8796 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -0.6146 |
| sortino_ratio | -0.1524 |
| max_drawdown | 0.3289 |
| cagr | -0.0702 |
| net_avg_win | 79.7681 |
| net_avg_loss | -95.0400 |
| avg_hold_time_bars | 14.5485 |
| exposure | 0.1977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
