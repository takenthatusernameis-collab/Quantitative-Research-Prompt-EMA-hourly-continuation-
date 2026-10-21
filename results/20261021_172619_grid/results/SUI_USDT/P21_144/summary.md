# EMA Hourly Continuation — SUI/USDT P21_144

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8836 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0569 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -0.7214 |
| sortino_ratio | -0.1997 |
| max_drawdown | 0.3545 |
| cagr | -0.0908 |
| net_avg_win | 84.4914 |
| net_avg_loss | -101.4620 |
| avg_hold_time_bars | 28.6280 |
| exposure | 0.4828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
