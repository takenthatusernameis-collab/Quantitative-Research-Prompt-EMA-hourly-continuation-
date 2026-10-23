# EMA Hourly Continuation — ZETA/USDT P20_34

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1153 |
| net_profit_factor | 0.3876 |
| net_win_rate | 0.4241 |
| gross_profit_factor | 0.8011 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -9.9531 |
| sortino_ratio | -4.7755 |
| max_drawdown | 0.9975 |
| cagr | -0.9073 |
| net_avg_win | 12.9127 |
| net_avg_loss | -24.5324 |
| avg_hold_time_bars | 2.8959 |
| exposure | 0.1511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
