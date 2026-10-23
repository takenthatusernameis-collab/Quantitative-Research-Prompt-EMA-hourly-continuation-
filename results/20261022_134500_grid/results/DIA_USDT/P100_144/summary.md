# EMA Hourly Continuation — DIA/USDT P100_144

**Symbol:** DIA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.5806 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 1.0900 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -4.2007 |
| sortino_ratio | -1.2918 |
| max_drawdown | 0.8067 |
| cagr | -0.4661 |
| net_avg_win | 48.0442 |
| net_avg_loss | -76.1002 |
| avg_hold_time_bars | 4.4268 |
| exposure | 0.0958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
