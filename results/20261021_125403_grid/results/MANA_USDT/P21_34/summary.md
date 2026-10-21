# EMA Hourly Continuation — MANA/USDT P21_34

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7330 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0790 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -1.5470 |
| sortino_ratio | -0.3919 |
| max_drawdown | 0.3596 |
| cagr | -0.1626 |
| net_avg_win | 61.3067 |
| net_avg_loss | -92.2346 |
| avg_hold_time_bars | 5.0586 |
| exposure | 0.0706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
