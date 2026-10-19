# EMA Hourly Continuation — CHZ/USDT P55_200

**Symbol:** CHZ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6964 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 1.0137 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.9479 |
| sortino_ratio | -0.5114 |
| max_drawdown | 0.4683 |
| cagr | -0.2136 |
| net_avg_win | 61.1502 |
| net_avg_loss | -86.7844 |
| avg_hold_time_bars | 24.1842 |
| exposure | 0.3760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
