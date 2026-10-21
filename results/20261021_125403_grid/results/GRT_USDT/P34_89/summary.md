# EMA Hourly Continuation — GRT/USDT P34_89

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.7726 |
| sortino_ratio | -0.5320 |
| max_drawdown | 0.4808 |
| cagr | -0.2171 |
| net_avg_win | 63.5139 |
| net_avg_loss | -84.7399 |
| avg_hold_time_bars | 10.2789 |
| exposure | 0.2051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
