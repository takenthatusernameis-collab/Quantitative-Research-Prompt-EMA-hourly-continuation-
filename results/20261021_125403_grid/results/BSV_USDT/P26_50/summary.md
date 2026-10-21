# EMA Hourly Continuation — BSV/USDT P26_50

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.5887 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.4335 |
| sortino_ratio | -1.0448 |
| max_drawdown | 0.6973 |
| cagr | -0.3787 |
| net_avg_win | 47.0720 |
| net_avg_loss | -70.9303 |
| avg_hold_time_bars | 6.3104 |
| exposure | 0.1294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
