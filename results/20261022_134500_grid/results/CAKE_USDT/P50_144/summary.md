# EMA Hourly Continuation — CAKE/USDT P50_144

**Symbol:** CAKE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.5223 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8938 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -4.4227 |
| sortino_ratio | -1.3048 |
| max_drawdown | 0.8141 |
| cagr | -0.4713 |
| net_avg_win | 43.6313 |
| net_avg_loss | -70.2015 |
| avg_hold_time_bars | 14.0091 |
| exposure | 0.2789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
