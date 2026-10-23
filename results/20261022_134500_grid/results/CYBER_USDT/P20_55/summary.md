# EMA Hourly Continuation — CYBER/USDT P20_55

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.5586 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -6.8533 |
| sortino_ratio | -2.9213 |
| max_drawdown | 0.9727 |
| cagr | -0.7606 |
| net_avg_win | 30.3874 |
| net_avg_loss | -42.6132 |
| avg_hold_time_bars | 6.6377 |
| exposure | 0.2782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
