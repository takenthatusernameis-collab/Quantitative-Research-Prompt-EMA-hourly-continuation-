# EMA Hourly Continuation — SUI/USDT P55_144

**Symbol:** SUI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6139 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.8109 |
| sortino_ratio | -1.2266 |
| max_drawdown | 0.7850 |
| cagr | -0.4447 |
| net_avg_win | 49.8822 |
| net_avg_loss | -71.8990 |
| avg_hold_time_bars | 9.5248 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
