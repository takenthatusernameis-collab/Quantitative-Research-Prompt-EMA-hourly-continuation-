# EMA Hourly Continuation — FIL/USDT P100_200

**Symbol:** FIL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5770 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9819 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -3.6624 |
| sortino_ratio | -1.0125 |
| max_drawdown | 0.7307 |
| cagr | -0.3923 |
| net_avg_win | 52.0650 |
| net_avg_loss | -82.7119 |
| avg_hold_time_bars | 8.3069 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
