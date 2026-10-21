# EMA Hourly Continuation — OP/USDT P20_50

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7224 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9568 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -2.0556 |
| sortino_ratio | -0.6479 |
| max_drawdown | 0.5331 |
| cagr | -0.2572 |
| net_avg_win | 57.0424 |
| net_avg_loss | -77.6670 |
| avg_hold_time_bars | 7.9649 |
| exposure | 0.1752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
