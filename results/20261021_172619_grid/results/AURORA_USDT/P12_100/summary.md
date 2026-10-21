# EMA Hourly Continuation — AURORA/USDT P12_100

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7613 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9566 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -1.8609 |
| sortino_ratio | -0.5615 |
| max_drawdown | 0.4928 |
| cagr | -0.2279 |
| net_avg_win | 69.8706 |
| net_avg_loss | -87.3724 |
| avg_hold_time_bars | 26.2483 |
| exposure | 0.5333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
