# EMA Hourly Continuation — ONDO/USDT P34_89

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.5718 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8768 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -5.1777 |
| sortino_ratio | -1.9133 |
| max_drawdown | 0.9063 |
| cagr | -0.6057 |
| net_avg_win | 38.2930 |
| net_avg_loss | -55.3703 |
| avg_hold_time_bars | 7.0661 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
