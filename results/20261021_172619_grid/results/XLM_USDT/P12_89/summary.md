# EMA Hourly Continuation — XLM/USDT P12_89

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8119 |
| net_win_rate | 0.5199 |
| gross_profit_factor | 1.0751 |
| gross_win_rate | 0.5199 |
| sharpe_ratio | -1.3615 |
| sortino_ratio | -0.4390 |
| max_drawdown | 0.4395 |
| cagr | -0.1840 |
| net_avg_win | 66.1316 |
| net_avg_loss | -88.2135 |
| avg_hold_time_bars | 23.2749 |
| exposure | 0.5311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
