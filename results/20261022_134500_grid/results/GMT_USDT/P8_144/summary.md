# EMA Hourly Continuation — GMT/USDT P8_144

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7128 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0242 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.9565 |
| sortino_ratio | -0.5296 |
| max_drawdown | 0.5149 |
| cagr | -0.2275 |
| net_avg_win | 62.9780 |
| net_avg_loss | -88.8255 |
| avg_hold_time_bars | 46.8000 |
| exposure | 0.7977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
