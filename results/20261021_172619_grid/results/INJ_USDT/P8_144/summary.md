# EMA Hourly Continuation — INJ/USDT P8_144

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7853 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9076 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -1.4127 |
| sortino_ratio | -0.3722 |
| max_drawdown | 0.3708 |
| cagr | -0.1584 |
| net_avg_win | 78.8885 |
| net_avg_loss | -90.9639 |
| avg_hold_time_bars | 48.0146 |
| exposure | 0.7486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
