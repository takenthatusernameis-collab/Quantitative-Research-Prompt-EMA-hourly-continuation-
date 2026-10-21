# EMA Hourly Continuation — T/USDT P144_200

**Symbol:** T/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9957 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -2.2932 |
| sortino_ratio | -0.5236 |
| max_drawdown | 0.4529 |
| cagr | -0.2127 |
| net_avg_win | 58.9786 |
| net_avg_loss | -94.1759 |
| avg_hold_time_bars | 7.8735 |
| exposure | 0.0901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
