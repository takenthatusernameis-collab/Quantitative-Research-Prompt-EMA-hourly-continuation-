# EMA Hourly Continuation — ONT/USDT P12_34

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1263 |
| net_profit_factor | 0.4579 |
| net_win_rate | 0.4109 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -10.6691 |
| sortino_ratio | -5.3171 |
| max_drawdown | 0.9990 |
| cagr | -0.9348 |
| net_avg_win | 16.2582 |
| net_avg_loss | -24.7685 |
| avg_hold_time_bars | 4.0721 |
| exposure | 0.2327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
