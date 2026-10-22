# EMA Hourly Continuation — JTO/USDT P26_34

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1060 |
| net_profit_factor | 0.3772 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.8325 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -9.8338 |
| sortino_ratio | -4.5496 |
| max_drawdown | 0.9969 |
| cagr | -0.8989 |
| net_avg_win | 13.1805 |
| net_avg_loss | -26.5865 |
| avg_hold_time_bars | 2.3406 |
| exposure | 0.1128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
