# EMA Hourly Continuation — GMEE/USDT P26_50

**Symbol:** GMEE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.4171 |
| net_win_rate | 0.4205 |
| gross_profit_factor | 0.6780 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -8.0375 |
| sortino_ratio | -3.4996 |
| max_drawdown | 0.9870 |
| cagr | -0.8218 |
| net_avg_win | 17.5659 |
| net_avg_loss | -30.5596 |
| avg_hold_time_bars | 4.2186 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
