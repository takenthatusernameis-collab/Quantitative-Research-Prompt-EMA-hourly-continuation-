# EMA Hourly Continuation — RAY/USDT P26_200

**Symbol:** RAY/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8308 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -0.9592 |
| sortino_ratio | -0.2299 |
| max_drawdown | 0.3228 |
| cagr | -0.1016 |
| net_avg_win | 82.7305 |
| net_avg_loss | -98.8749 |
| avg_hold_time_bars | 43.5623 |
| exposure | 0.5564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
