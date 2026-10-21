# EMA Hourly Continuation — ENJ/USDT P8_89

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.8332 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 1.0161 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.3688 |
| sortino_ratio | -0.4440 |
| max_drawdown | 0.4916 |
| cagr | -0.1868 |
| net_avg_win | 78.4105 |
| net_avg_loss | -94.8381 |
| avg_hold_time_bars | 26.7500 |
| exposure | 0.6246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
