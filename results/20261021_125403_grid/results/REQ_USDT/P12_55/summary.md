# EMA Hourly Continuation — REQ/USDT P12_55

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5953 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.8611 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -5.3770 |
| sortino_ratio | -2.0087 |
| max_drawdown | 0.9065 |
| cagr | -0.6081 |
| net_avg_win | 44.2189 |
| net_avg_loss | -57.9236 |
| avg_hold_time_bars | 11.1033 |
| exposure | 0.3467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
