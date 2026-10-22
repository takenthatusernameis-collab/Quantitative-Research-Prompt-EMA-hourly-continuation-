# EMA Hourly Continuation — WOO/USDT P12_89

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.8365 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 1.0124 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -1.4667 |
| sortino_ratio | -0.4769 |
| max_drawdown | 0.5245 |
| cagr | -0.1988 |
| net_avg_win | 84.6574 |
| net_avg_loss | -100.8086 |
| avg_hold_time_bars | 23.2727 |
| exposure | 0.5469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
