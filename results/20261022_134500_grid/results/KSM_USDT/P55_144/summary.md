# EMA Hourly Continuation — KSM/USDT P55_144

**Symbol:** KSM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.5528 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.9324 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -4.3859 |
| sortino_ratio | -1.3628 |
| max_drawdown | 0.8243 |
| cagr | -0.4863 |
| net_avg_win | 44.2342 |
| net_avg_loss | -68.2857 |
| avg_hold_time_bars | 10.8925 |
| exposure | 0.2441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
