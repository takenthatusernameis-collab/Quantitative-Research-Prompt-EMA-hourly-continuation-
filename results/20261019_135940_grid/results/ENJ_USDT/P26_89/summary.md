# EMA Hourly Continuation — ENJ/USDT P26_89

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6535 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -4.2500 |
| sortino_ratio | -1.5811 |
| max_drawdown | 0.8630 |
| cagr | -0.5314 |
| net_avg_win | 48.3345 |
| net_avg_loss | -67.4631 |
| avg_hold_time_bars | 10.8233 |
| exposure | 0.3424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
