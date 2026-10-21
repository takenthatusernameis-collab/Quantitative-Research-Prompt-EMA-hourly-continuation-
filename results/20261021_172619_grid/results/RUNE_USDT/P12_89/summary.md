# EMA Hourly Continuation — RUNE/USDT P12_89

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8152 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0124 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -1.2836 |
| sortino_ratio | -0.3706 |
| max_drawdown | 0.3892 |
| cagr | -0.1584 |
| net_avg_win | 75.6587 |
| net_avg_loss | -94.6512 |
| avg_hold_time_bars | 33.4951 |
| exposure | 0.6181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
