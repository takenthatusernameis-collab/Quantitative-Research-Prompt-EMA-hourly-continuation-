# EMA Hourly Continuation — AMP/USDT P21_144

**Symbol:** AMP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5280 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.6652 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -4.0659 |
| sortino_ratio | -1.2667 |
| max_drawdown | 0.7861 |
| cagr | -0.4444 |
| net_avg_win | 42.9418 |
| net_avg_loss | -57.1542 |
| avg_hold_time_bars | 22.1355 |
| exposure | 0.4900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
