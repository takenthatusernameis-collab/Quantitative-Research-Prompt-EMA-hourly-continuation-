# EMA Hourly Continuation — DODO/USDT P55_144

**Symbol:** DODO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8623 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.5141 |
| sortino_ratio | -0.7063 |
| max_drawdown | 0.5716 |
| cagr | -0.2776 |
| net_avg_win | 66.0133 |
| net_avg_loss | -82.7605 |
| avg_hold_time_bars | 12.9135 |
| exposure | 0.2296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
