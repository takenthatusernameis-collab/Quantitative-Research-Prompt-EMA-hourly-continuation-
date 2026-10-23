# EMA Hourly Continuation — AMP/USDT P100_144

**Symbol:** AMP/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.2220 |
| net_win_rate | 0.3501 |
| gross_profit_factor | 0.5356 |
| gross_win_rate | 0.3828 |
| sharpe_ratio | -9.6749 |
| sortino_ratio | -3.5913 |
| max_drawdown | 0.9903 |
| cagr | -0.8419 |
| net_avg_win | 11.9732 |
| net_avg_loss | -29.0600 |
| avg_hold_time_bars | 4.1558 |
| exposure | 0.1273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
