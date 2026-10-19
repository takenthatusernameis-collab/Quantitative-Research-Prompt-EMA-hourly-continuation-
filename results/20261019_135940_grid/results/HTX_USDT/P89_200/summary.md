# EMA Hourly Continuation — HTX/USDT P89_200

**Symbol:** HTX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.2990 |
| net_win_rate | 0.3372 |
| gross_profit_factor | 0.7579 |
| gross_win_rate | 0.3724 |
| sharpe_ratio | -8.8028 |
| sortino_ratio | -2.6601 |
| max_drawdown | 0.9726 |
| cagr | -0.7577 |
| net_avg_win | 28.7904 |
| net_avg_loss | -48.9966 |
| avg_hold_time_bars | 11.7119 |
| exposure | 0.2263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
