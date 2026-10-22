# EMA Hourly Continuation — API3/USDT P12_200

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8601 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -0.8279 |
| sortino_ratio | -0.2143 |
| max_drawdown | 0.3398 |
| cagr | -0.0962 |
| net_avg_win | 83.5550 |
| net_avg_loss | -98.9449 |
| avg_hold_time_bars | 48.6024 |
| exposure | 0.7224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
