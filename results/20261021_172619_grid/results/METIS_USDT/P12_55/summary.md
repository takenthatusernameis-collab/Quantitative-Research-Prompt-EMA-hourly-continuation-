# EMA Hourly Continuation — METIS/USDT P12_55

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6865 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8635 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -3.1960 |
| sortino_ratio | -1.1540 |
| max_drawdown | 0.7530 |
| cagr | -0.4121 |
| net_avg_win | 54.3006 |
| net_avg_loss | -67.3144 |
| avg_hold_time_bars | 13.0464 |
| exposure | 0.3831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
