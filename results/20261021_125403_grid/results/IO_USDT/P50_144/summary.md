# EMA Hourly Continuation — IO/USDT P50_144

**Symbol:** IO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8078 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9672 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.2726 |
| sortino_ratio | -0.3400 |
| max_drawdown | 0.3439 |
| cagr | -0.1459 |
| net_avg_win | 81.0671 |
| net_avg_loss | -96.7508 |
| avg_hold_time_bars | 16.3750 |
| exposure | 0.2600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
