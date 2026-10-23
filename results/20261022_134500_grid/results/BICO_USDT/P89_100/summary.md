# EMA Hourly Continuation — BICO/USDT P89_100

**Symbol:** BICO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.3037 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.7429 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -7.7566 |
| sortino_ratio | -2.6792 |
| max_drawdown | 0.9659 |
| cagr | -0.7393 |
| net_avg_win | 17.8507 |
| net_avg_loss | -39.8588 |
| avg_hold_time_bars | 3.0668 |
| exposure | 0.0814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
