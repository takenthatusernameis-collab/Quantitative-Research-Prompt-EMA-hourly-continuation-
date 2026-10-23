# EMA Hourly Continuation — DEGEN/USDT P8_50

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1057 |
| net_profit_factor | 0.7001 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -5.0006 |
| sortino_ratio | -2.2883 |
| max_drawdown | 0.9367 |
| cagr | -0.6644 |
| net_avg_win | 44.3682 |
| net_avg_loss | -55.1888 |
| avg_hold_time_bars | 9.8874 |
| exposure | 0.4758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
