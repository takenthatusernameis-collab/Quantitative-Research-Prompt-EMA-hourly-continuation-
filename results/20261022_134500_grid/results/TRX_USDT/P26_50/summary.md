# EMA Hourly Continuation — TRX/USDT P26_50

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 806 |
| net_profit_factor | 0.1579 |
| net_win_rate | 0.3213 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -14.2199 |
| sortino_ratio | -6.2316 |
| max_drawdown | 0.9998 |
| cagr | -0.9676 |
| net_avg_win | 7.2390 |
| net_avg_loss | -21.7058 |
| avg_hold_time_bars | 3.9243 |
| exposure | 0.1438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
