# EMA Hourly Continuation — NYM/USDT P12_200

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.4510 |
| net_win_rate | 0.3645 |
| gross_profit_factor | 0.6034 |
| gross_win_rate | 0.3679 |
| sharpe_ratio | -4.2738 |
| sortino_ratio | -1.0396 |
| max_drawdown | 0.7101 |
| cagr | -0.3845 |
| net_avg_win | 53.0891 |
| net_avg_loss | -67.5281 |
| avg_hold_time_bars | 51.1672 |
| exposure | 0.6954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
