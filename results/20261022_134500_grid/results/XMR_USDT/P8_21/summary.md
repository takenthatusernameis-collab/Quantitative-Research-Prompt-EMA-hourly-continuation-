# EMA Hourly Continuation — XMR/USDT P8_21

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1973 |
| net_profit_factor | 0.1500 |
| net_win_rate | 0.3568 |
| gross_profit_factor | 0.4851 |
| gross_win_rate | 0.3751 |
| sharpe_ratio | -18.4806 |
| sortino_ratio | -11.7994 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 2.5070 |
| net_avg_loss | -9.2710 |
| avg_hold_time_bars | 2.2342 |
| exposure | 0.2004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
