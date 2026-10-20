# EMA Hourly Continuation — ENJ/USDT P21_34

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1125 |
| net_profit_factor | 0.3418 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.7921 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -10.5292 |
| sortino_ratio | -5.0307 |
| max_drawdown | 0.9984 |
| cagr | -0.9219 |
| net_avg_win | 10.8932 |
| net_avg_loss | -23.3723 |
| avg_hold_time_bars | 2.5102 |
| exposure | 0.1284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
