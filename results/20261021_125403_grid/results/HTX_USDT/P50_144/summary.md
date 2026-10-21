# EMA Hourly Continuation — HTX/USDT P50_144

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.4415 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.7080 |
| gross_win_rate | 0.3803 |
| sharpe_ratio | -5.6615 |
| sortino_ratio | -1.5338 |
| max_drawdown | 0.8444 |
| cagr | -0.5159 |
| net_avg_win | 49.1653 |
| net_avg_loss | -68.3336 |
| avg_hold_time_bars | 18.2169 |
| exposure | 0.2927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
