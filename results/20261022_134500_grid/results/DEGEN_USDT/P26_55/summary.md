# EMA Hourly Continuation — DEGEN/USDT P26_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.5613 |
| net_win_rate | 0.4281 |
| gross_profit_factor | 0.8364 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -6.5694 |
| sortino_ratio | -2.7198 |
| max_drawdown | 0.9646 |
| cagr | -0.7341 |
| net_avg_win | 33.1561 |
| net_avg_loss | -44.2113 |
| avg_hold_time_bars | 4.4868 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
