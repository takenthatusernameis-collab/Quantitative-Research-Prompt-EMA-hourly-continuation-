# EMA Hourly Continuation — BOME/USDT P55_144

**Symbol:** BOME/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.5993 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.8419 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.0657 |
| sortino_ratio | -0.9721 |
| max_drawdown | 0.7041 |
| cagr | -0.3677 |
| net_avg_win | 42.7961 |
| net_avg_loss | -64.3992 |
| avg_hold_time_bars | 11.5496 |
| exposure | 0.2646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
