# EMA Hourly Continuation — SHIB/USDT P21_144

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.6779 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 1.0446 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -3.2739 |
| sortino_ratio | -1.0822 |
| max_drawdown | 0.7326 |
| cagr | -0.4017 |
| net_avg_win | 56.6997 |
| net_avg_loss | -80.9335 |
| avg_hold_time_bars | 18.6508 |
| exposure | 0.4637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
