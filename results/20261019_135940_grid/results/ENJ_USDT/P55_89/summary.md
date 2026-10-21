# EMA Hourly Continuation — ENJ/USDT P55_89

**Symbol:** ENJ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5679 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -5.1788 |
| sortino_ratio | -1.8888 |
| max_drawdown | 0.9024 |
| cagr | -0.5966 |
| net_avg_win | 37.6252 |
| net_avg_loss | -60.1214 |
| avg_hold_time_bars | 4.2970 |
| exposure | 0.1283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
