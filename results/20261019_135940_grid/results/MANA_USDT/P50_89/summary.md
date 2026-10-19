# EMA Hourly Continuation — MANA/USDT P50_89

**Symbol:** MANA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.4145 |
| net_win_rate | 0.4112 |
| gross_profit_factor | 0.7959 |
| gross_win_rate | 0.4298 |
| sharpe_ratio | -7.9727 |
| sortino_ratio | -2.9617 |
| max_drawdown | 0.9780 |
| cagr | -0.7792 |
| net_avg_win | 24.1110 |
| net_avg_loss | -40.6194 |
| avg_hold_time_bars | 4.5487 |
| exposure | 0.1443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
