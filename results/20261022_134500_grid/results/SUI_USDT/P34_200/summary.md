# EMA Hourly Continuation — SUI/USDT P34_200

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7303 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.1123 |
| sortino_ratio | -0.5831 |
| max_drawdown | 0.5781 |
| cagr | -0.2463 |
| net_avg_win | 70.9644 |
| net_avg_loss | -97.1734 |
| avg_hold_time_bars | 26.8686 |
| exposure | 0.4739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
