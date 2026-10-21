# EMA Hourly Continuation — SAFE/USDT P12_50

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.7779 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 0.9862 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -1.9182 |
| sortino_ratio | -0.6937 |
| max_drawdown | 0.5592 |
| cagr | -0.2743 |
| net_avg_win | 60.7827 |
| net_avg_loss | -78.3883 |
| avg_hold_time_bars | 12.1675 |
| exposure | 0.3527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
