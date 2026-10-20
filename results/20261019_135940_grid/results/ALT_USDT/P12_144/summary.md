# EMA Hourly Continuation — ALT/USDT P12_144

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6749 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9073 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -2.7969 |
| sortino_ratio | -0.8731 |
| max_drawdown | 0.6626 |
| cagr | -0.3410 |
| net_avg_win | 57.8355 |
| net_avg_loss | -75.9184 |
| avg_hold_time_bars | 29.4617 |
| exposure | 0.6642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
