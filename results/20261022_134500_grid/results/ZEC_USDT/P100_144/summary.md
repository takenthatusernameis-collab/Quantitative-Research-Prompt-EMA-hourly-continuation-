# EMA Hourly Continuation — ZEC/USDT P100_144

**Symbol:** ZEC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.4250 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.7917 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -4.7073 |
| sortino_ratio | -1.4793 |
| max_drawdown | 0.8416 |
| cagr | -0.5155 |
| net_avg_win | 27.0483 |
| net_avg_loss | -54.1749 |
| avg_hold_time_bars | 3.9438 |
| exposure | 0.0893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
