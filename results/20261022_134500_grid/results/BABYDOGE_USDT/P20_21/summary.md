# EMA Hourly Continuation — BABYDOGE/USDT P20_21

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 6 |
| net_profit_factor | 0.4662 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.4964 |
| gross_win_rate | 0.3333 |
| sharpe_ratio | -0.5633 |
| sortino_ratio | -0.0191 |
| max_drawdown | 0.0222 |
| cagr | -0.0089 |
| net_avg_win | 97.1477 |
| net_avg_loss | -104.1824 |
| avg_hold_time_bars | 3.1667 |
| exposure | 0.0009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
