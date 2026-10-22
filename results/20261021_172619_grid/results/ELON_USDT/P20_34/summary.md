# EMA Hourly Continuation — ELON/USDT P20_34

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6669 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9586 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.2002 |
| sortino_ratio | -0.5400 |
| max_drawdown | 0.4913 |
| cagr | -0.2178 |
| net_avg_win | 64.4566 |
| net_avg_loss | -92.7613 |
| avg_hold_time_bars | 5.7740 |
| exposure | 0.0766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
