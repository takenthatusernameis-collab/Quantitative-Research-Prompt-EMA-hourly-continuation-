# EMA Hourly Continuation — MTL/USDT P21_55

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.4894 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -7.0035 |
| sortino_ratio | -2.8567 |
| max_drawdown | 0.9706 |
| cagr | -0.7514 |
| net_avg_win | 25.6139 |
| net_avg_loss | -40.4240 |
| avg_hold_time_bars | 8.1657 |
| exposure | 0.3078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
