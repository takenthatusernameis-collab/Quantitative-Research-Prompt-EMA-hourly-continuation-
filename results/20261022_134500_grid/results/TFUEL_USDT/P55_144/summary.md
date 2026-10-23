# EMA Hourly Continuation — TFUEL/USDT P55_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.4453 |
| net_win_rate | 0.3980 |
| gross_profit_factor | 0.7701 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -6.7542 |
| sortino_ratio | -2.3577 |
| max_drawdown | 0.9452 |
| cagr | -0.6827 |
| net_avg_win | 31.0878 |
| net_avg_loss | -46.1592 |
| avg_hold_time_bars | 9.0701 |
| exposure | 0.2516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
