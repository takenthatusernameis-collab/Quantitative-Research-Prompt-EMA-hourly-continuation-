# EMA Hourly Continuation — AMP/USDT P8_20

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2082 |
| net_profit_factor | 0.2052 |
| net_win_rate | 0.3353 |
| gross_profit_factor | 0.5865 |
| gross_win_rate | 0.3809 |
| sharpe_ratio | -18.9445 |
| sortino_ratio | -12.3675 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 3.6999 |
| net_avg_loss | -9.0914 |
| avg_hold_time_bars | 2.6273 |
| exposure | 0.2486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
