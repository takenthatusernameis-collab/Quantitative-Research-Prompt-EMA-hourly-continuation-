# EMA Hourly Continuation — ENJ/USDT P34_200

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9061 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0919 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.4788 |
| sortino_ratio | -0.1163 |
| max_drawdown | 0.2202 |
| cagr | -0.0555 |
| net_avg_win | 86.3391 |
| net_avg_loss | -104.3243 |
| avg_hold_time_bars | 40.2997 |
| exposure | 0.5234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
