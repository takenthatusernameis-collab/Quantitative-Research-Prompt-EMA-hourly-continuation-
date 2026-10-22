# EMA Hourly Continuation — EGLD/USDT P12_55

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -6.1827 |
| sortino_ratio | -2.7187 |
| max_drawdown | 0.9666 |
| cagr | -0.7356 |
| net_avg_win | 27.7631 |
| net_avg_loss | -42.4844 |
| avg_hold_time_bars | 8.6988 |
| exposure | 0.3899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
