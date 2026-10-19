# EMA Hourly Continuation — XTZ/USDT P26_50

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.3919 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -9.1910 |
| sortino_ratio | -4.1413 |
| max_drawdown | 0.9945 |
| cagr | -0.8725 |
| net_avg_win | 14.7288 |
| net_avg_loss | -28.6848 |
| avg_hold_time_bars | 3.8050 |
| exposure | 0.1738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
