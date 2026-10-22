# EMA Hourly Continuation — SUN/USDT P55_144

**Symbol:** SUN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.3542 |
| net_win_rate | 0.3797 |
| gross_profit_factor | 0.7734 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -7.2345 |
| sortino_ratio | -2.1062 |
| max_drawdown | 0.9400 |
| cagr | -0.6710 |
| net_avg_win | 32.0010 |
| net_avg_loss | -55.3101 |
| avg_hold_time_bars | 13.8349 |
| exposure | 0.2655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
