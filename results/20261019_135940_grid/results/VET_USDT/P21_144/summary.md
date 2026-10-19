# EMA Hourly Continuation — VET/USDT P21_144

**Symbol:** VET/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6373 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -3.0865 |
| sortino_ratio | -0.9894 |
| max_drawdown | 0.7134 |
| cagr | -0.3777 |
| net_avg_win | 48.3442 |
| net_avg_loss | -72.1539 |
| avg_hold_time_bars | 22.0231 |
| exposure | 0.5195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
