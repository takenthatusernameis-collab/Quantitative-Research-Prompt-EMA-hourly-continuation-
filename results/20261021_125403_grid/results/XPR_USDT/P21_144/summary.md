# EMA Hourly Continuation — XPR/USDT P21_144

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6801 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8385 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -2.0633 |
| sortino_ratio | -0.5369 |
| max_drawdown | 0.4813 |
| cagr | -0.2191 |
| net_avg_win | 63.0517 |
| net_avg_loss | -80.3459 |
| avg_hold_time_bars | 29.7143 |
| exposure | 0.4538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
