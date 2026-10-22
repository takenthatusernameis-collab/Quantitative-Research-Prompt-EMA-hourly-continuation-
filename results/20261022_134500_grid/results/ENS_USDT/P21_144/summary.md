# EMA Hourly Continuation — ENS/USDT P21_144

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6555 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.5861 |
| sortino_ratio | -0.7817 |
| max_drawdown | 0.6340 |
| cagr | -0.3107 |
| net_avg_win | 51.5736 |
| net_avg_loss | -74.3637 |
| avg_hold_time_bars | 27.1779 |
| exposure | 0.5695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
