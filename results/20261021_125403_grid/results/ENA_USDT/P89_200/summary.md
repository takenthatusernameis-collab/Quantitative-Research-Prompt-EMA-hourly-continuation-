# EMA Hourly Continuation — ENA/USDT P89_200

**Symbol:** ENA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.8040 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.0306 |
| sortino_ratio | -0.2253 |
| max_drawdown | 0.2700 |
| cagr | -0.0995 |
| net_avg_win | 83.3140 |
| net_avg_loss | -97.6262 |
| avg_hold_time_bars | 14.7362 |
| exposure | 0.1574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
