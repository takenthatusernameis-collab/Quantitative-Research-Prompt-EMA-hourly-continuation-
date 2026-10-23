# EMA Hourly Continuation — LUNA/USDT P12_89

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.4668 |
| net_win_rate | 0.4199 |
| gross_profit_factor | 0.8032 |
| gross_win_rate | 0.4334 |
| sharpe_ratio | -7.6764 |
| sortino_ratio | -3.2292 |
| max_drawdown | 0.9820 |
| cagr | -0.7974 |
| net_avg_win | 22.9201 |
| net_avg_loss | -35.5474 |
| avg_hold_time_bars | 11.8903 |
| exposure | 0.4826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
