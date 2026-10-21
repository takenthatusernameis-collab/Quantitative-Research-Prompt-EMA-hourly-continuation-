# EMA Hourly Continuation — PEPE/USDT P26_34

**Symbol:** PEPE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.7214 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9535 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -1.2238 |
| sortino_ratio | -0.1997 |
| max_drawdown | 0.2452 |
| cagr | -0.0876 |
| net_avg_win | 84.5165 |
| net_avg_loss | -110.1663 |
| avg_hold_time_bars | 4.7692 |
| exposure | 0.0282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
