# EMA Hourly Continuation — RPL/USDT P34_89

**Symbol:** RPL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.6160 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9349 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -3.9973 |
| sortino_ratio | -1.4250 |
| max_drawdown | 0.8197 |
| cagr | -0.4895 |
| net_avg_win | 43.8172 |
| net_avg_loss | -62.1839 |
| avg_hold_time_bars | 10.2793 |
| exposure | 0.2982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
