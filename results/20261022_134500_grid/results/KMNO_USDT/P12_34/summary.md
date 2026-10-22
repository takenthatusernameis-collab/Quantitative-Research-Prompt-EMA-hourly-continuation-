# EMA Hourly Continuation — KMNO/USDT P12_34

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.5234 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.8838 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -7.0770 |
| sortino_ratio | -3.2730 |
| max_drawdown | 0.9812 |
| cagr | -0.7997 |
| net_avg_win | 21.9470 |
| net_avg_loss | -35.7434 |
| avg_hold_time_bars | 4.8416 |
| exposure | 0.2385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
