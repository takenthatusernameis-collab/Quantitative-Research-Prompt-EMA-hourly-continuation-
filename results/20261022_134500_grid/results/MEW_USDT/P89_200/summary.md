# EMA Hourly Continuation — MEW/USDT P89_200

**Symbol:** MEW/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.6282 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8932 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -3.1818 |
| sortino_ratio | -0.8760 |
| max_drawdown | 0.6713 |
| cagr | -0.3436 |
| net_avg_win | 62.3093 |
| net_avg_loss | -83.9956 |
| avg_hold_time_bars | 13.3860 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
