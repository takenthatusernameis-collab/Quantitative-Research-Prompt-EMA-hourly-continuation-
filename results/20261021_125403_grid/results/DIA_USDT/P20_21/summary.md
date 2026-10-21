# EMA Hourly Continuation — DIA/USDT P20_21

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.6578 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0083 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.9434 |
| sortino_ratio | -0.4219 |
| max_drawdown | 0.4125 |
| cagr | -0.1751 |
| net_avg_win | 64.2819 |
| net_avg_loss | -99.4529 |
| avg_hold_time_bars | 4.2807 |
| exposure | 0.0442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
