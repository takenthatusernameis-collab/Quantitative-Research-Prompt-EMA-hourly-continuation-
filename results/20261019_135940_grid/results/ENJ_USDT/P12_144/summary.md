# EMA Hourly Continuation — ENJ/USDT P12_144

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.5739 |
| sortino_ratio | -0.7339 |
| max_drawdown | 0.6114 |
| cagr | -0.2977 |
| net_avg_win | 57.9319 |
| net_avg_loss | -80.9806 |
| avg_hold_time_bars | 37.7633 |
| exposure | 0.7106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
