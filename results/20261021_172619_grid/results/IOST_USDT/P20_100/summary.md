# EMA Hourly Continuation — IOST/USDT P20_100

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.5257 |
| gross_profit_factor | 1.0985 |
| gross_win_rate | 0.5257 |
| sharpe_ratio | -1.2367 |
| sortino_ratio | -0.3930 |
| max_drawdown | 0.4154 |
| cagr | -0.1673 |
| net_avg_win | 71.1683 |
| net_avg_loss | -94.8281 |
| avg_hold_time_bars | 17.4784 |
| exposure | 0.3869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
