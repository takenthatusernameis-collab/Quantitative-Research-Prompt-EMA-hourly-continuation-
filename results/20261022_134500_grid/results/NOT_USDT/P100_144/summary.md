# EMA Hourly Continuation — NOT/USDT P100_144

**Symbol:** NOT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5271 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -4.2389 |
| sortino_ratio | -1.3652 |
| max_drawdown | 0.7989 |
| cagr | -0.4792 |
| net_avg_win | 36.9284 |
| net_avg_loss | -65.4235 |
| avg_hold_time_bars | 3.5835 |
| exposure | 0.0837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
