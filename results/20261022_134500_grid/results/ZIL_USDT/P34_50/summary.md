# EMA Hourly Continuation — ZIL/USDT P34_50

**Symbol:** ZIL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.3096 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.7912 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -9.9616 |
| sortino_ratio | -4.3843 |
| max_drawdown | 0.9962 |
| cagr | -0.8906 |
| net_avg_win | 11.2261 |
| net_avg_loss | -26.5736 |
| avg_hold_time_bars | 2.6567 |
| exposure | 0.1136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
