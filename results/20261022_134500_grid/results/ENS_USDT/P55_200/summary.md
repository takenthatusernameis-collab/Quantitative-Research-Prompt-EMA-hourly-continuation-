# EMA Hourly Continuation — ENS/USDT P55_200

**Symbol:** ENS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8642 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -3.1142 |
| sortino_ratio | -0.8408 |
| max_drawdown | 0.6588 |
| cagr | -0.3390 |
| net_avg_win | 48.1959 |
| net_avg_loss | -74.7354 |
| avg_hold_time_bars | 21.5532 |
| exposure | 0.3684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
