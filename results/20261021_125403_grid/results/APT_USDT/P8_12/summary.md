# EMA Hourly Continuation — APT/USDT P8_12

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.7595 |
| net_win_rate | 0.5179 |
| gross_profit_factor | 1.0686 |
| gross_win_rate | 0.5179 |
| sharpe_ratio | -1.1765 |
| sortino_ratio | -0.2369 |
| max_drawdown | 0.2585 |
| cagr | -0.1025 |
| net_avg_win | 74.3835 |
| net_avg_loss | -105.2340 |
| avg_hold_time_bars | 4.6667 |
| exposure | 0.0414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
