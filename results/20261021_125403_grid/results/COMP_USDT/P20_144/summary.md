# EMA Hourly Continuation — COMP/USDT P20_144

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 0.9973 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.6467 |
| sortino_ratio | -0.4860 |
| max_drawdown | 0.4741 |
| cagr | -0.2014 |
| net_avg_win | 66.0740 |
| net_avg_loss | -86.6430 |
| avg_hold_time_bars | 28.8525 |
| exposure | 0.5600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
