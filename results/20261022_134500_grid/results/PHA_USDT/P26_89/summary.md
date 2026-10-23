# EMA Hourly Continuation — PHA/USDT P26_89

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.4624 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.7466 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -5.3693 |
| sortino_ratio | -2.0268 |
| max_drawdown | 0.9201 |
| cagr | -0.6309 |
| net_avg_win | 24.3024 |
| net_avg_loss | -41.5568 |
| avg_hold_time_bars | 8.8899 |
| exposure | 0.2974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
