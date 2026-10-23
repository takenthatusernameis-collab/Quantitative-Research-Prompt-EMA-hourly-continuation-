# EMA Hourly Continuation — POKT/USDT P20_34

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1220 |
| net_profit_factor | 0.3590 |
| net_win_rate | 0.3566 |
| gross_profit_factor | 0.8108 |
| gross_win_rate | 0.3844 |
| sharpe_ratio | -12.4242 |
| sortino_ratio | -6.1269 |
| max_drawdown | 0.9996 |
| cagr | -0.9546 |
| net_avg_win | 12.8669 |
| net_avg_loss | -19.8637 |
| avg_hold_time_bars | 3.4951 |
| exposure | 0.1930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
