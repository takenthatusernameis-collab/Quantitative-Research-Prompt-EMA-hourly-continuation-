# EMA Hourly Continuation — TRB/USDT P89_200

**Symbol:** TRB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7059 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -1.7582 |
| sortino_ratio | -0.4251 |
| max_drawdown | 0.4133 |
| cagr | -0.1772 |
| net_avg_win | 67.0757 |
| net_avg_loss | -88.0582 |
| avg_hold_time_bars | 14.0173 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
