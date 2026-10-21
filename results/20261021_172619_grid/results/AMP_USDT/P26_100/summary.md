# EMA Hourly Continuation — AMP/USDT P26_100

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5170 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.6786 |
| gross_win_rate | 0.4077 |
| sharpe_ratio | -4.6048 |
| sortino_ratio | -1.4855 |
| max_drawdown | 0.8316 |
| cagr | -0.4972 |
| net_avg_win | 41.5049 |
| net_avg_loss | -55.2594 |
| avg_hold_time_bars | 14.2404 |
| exposure | 0.3366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
