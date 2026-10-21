# EMA Hourly Continuation — AR/USDT P21_144

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7428 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -1.7211 |
| sortino_ratio | -0.4628 |
| max_drawdown | 0.4448 |
| cagr | -0.1926 |
| net_avg_win | 71.4311 |
| net_avg_loss | -85.0346 |
| avg_hold_time_bars | 33.4050 |
| exposure | 0.5436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
