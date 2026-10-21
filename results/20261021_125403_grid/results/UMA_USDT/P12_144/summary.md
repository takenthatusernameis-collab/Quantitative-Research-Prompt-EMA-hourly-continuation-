# EMA Hourly Continuation — UMA/USDT P12_144

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.7966 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.4606 |
| sortino_ratio | -0.4495 |
| max_drawdown | 0.4321 |
| cagr | -0.1874 |
| net_avg_win | 68.2898 |
| net_avg_loss | -86.8408 |
| avg_hold_time_bars | 28.5616 |
| exposure | 0.6011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
