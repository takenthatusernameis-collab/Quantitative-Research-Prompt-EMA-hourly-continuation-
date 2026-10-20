# EMA Hourly Continuation — ENJ/USDT P34_200

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7186 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0551 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.9123 |
| sortino_ratio | -0.5264 |
| max_drawdown | 0.4837 |
| cagr | -0.2229 |
| net_avg_win | 61.1235 |
| net_avg_loss | -90.1220 |
| avg_hold_time_bars | 30.6588 |
| exposure | 0.5310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
