# EMA Hourly Continuation — QI/USDT P20_144

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5824 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.8695 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -3.9209 |
| sortino_ratio | -1.2093 |
| max_drawdown | 0.7827 |
| cagr | -0.4417 |
| net_avg_win | 49.2754 |
| net_avg_loss | -68.5637 |
| avg_hold_time_bars | 24.0144 |
| exposure | 0.5292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
