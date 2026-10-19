# EMA Hourly Continuation — WIF/USDT P55_144

**Symbol:** WIF/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6331 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9216 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -2.9239 |
| sortino_ratio | -0.9103 |
| max_drawdown | 0.6803 |
| cagr | -0.3494 |
| net_avg_win | 48.4784 |
| net_avg_loss | -72.2679 |
| avg_hold_time_bars | 10.6694 |
| exposure | 0.2347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
