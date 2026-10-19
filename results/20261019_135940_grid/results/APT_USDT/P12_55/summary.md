# EMA Hourly Continuation — APT/USDT P12_55

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -6.0453 |
| sortino_ratio | -2.6255 |
| max_drawdown | 0.9631 |
| cagr | -0.7243 |
| net_avg_win | 27.0070 |
| net_avg_loss | -41.7463 |
| avg_hold_time_bars | 9.0374 |
| exposure | 0.3956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
