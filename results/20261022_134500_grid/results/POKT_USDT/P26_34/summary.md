# EMA Hourly Continuation — POKT/USDT P26_34

**Symbol:** POKT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.2971 |
| net_win_rate | 0.3307 |
| gross_profit_factor | 0.8150 |
| gross_win_rate | 0.3780 |
| sharpe_ratio | -13.5210 |
| sortino_ratio | -6.4585 |
| max_drawdown | 0.9998 |
| cagr | -0.9651 |
| net_avg_win | 11.4195 |
| net_avg_loss | -18.9895 |
| avg_hold_time_bars | 3.1126 |
| exposure | 0.1576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
