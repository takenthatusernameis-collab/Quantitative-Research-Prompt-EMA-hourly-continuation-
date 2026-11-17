# EMA Hourly Continuation — NUM/USDT P34_89

**Symbol:** NUM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.4425 |
| net_win_rate | 0.3679 |
| gross_profit_factor | 0.6983 |
| gross_win_rate | 0.3778 |
| sharpe_ratio | -7.5039 |
| sortino_ratio | -2.8032 |
| max_drawdown | 0.9673 |
| cagr | -0.7397 |
| net_avg_win | 29.6049 |
| net_avg_loss | -38.9373 |
| avg_hold_time_bars | 8.6193 |
| exposure | 0.2758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
