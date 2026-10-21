# EMA Hourly Continuation — SAND/USDT P12_55

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.6405 |
| sortino_ratio | -0.9199 |
| max_drawdown | 0.6865 |
| cagr | -0.3446 |
| net_avg_win | 57.5107 |
| net_avg_loss | -74.3924 |
| avg_hold_time_bars | 13.7378 |
| exposure | 0.3715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
