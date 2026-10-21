# EMA Hourly Continuation — ONT/USDT P50_144

**Symbol:** ONT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6759 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -2.0857 |
| sortino_ratio | -0.5472 |
| max_drawdown | 0.4970 |
| cagr | -0.2231 |
| net_avg_win | 60.9964 |
| net_avg_loss | -80.7217 |
| avg_hold_time_bars | 17.6217 |
| exposure | 0.2719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
