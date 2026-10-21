# EMA Hourly Continuation — ACE/USDT P8_55

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7319 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -2.4285 |
| sortino_ratio | -0.8543 |
| max_drawdown | 0.6339 |
| cagr | -0.3248 |
| net_avg_win | 57.9856 |
| net_avg_loss | -74.2118 |
| avg_hold_time_bars | 17.8627 |
| exposure | 0.4947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
