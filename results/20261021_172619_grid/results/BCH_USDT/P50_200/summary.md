# EMA Hourly Continuation — BCH/USDT P50_200

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7821 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0069 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.2560 |
| sortino_ratio | -0.2980 |
| max_drawdown | 0.3260 |
| cagr | -0.1282 |
| net_avg_win | 75.8048 |
| net_avg_loss | -98.3456 |
| avg_hold_time_bars | 31.7372 |
| exposure | 0.3953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
