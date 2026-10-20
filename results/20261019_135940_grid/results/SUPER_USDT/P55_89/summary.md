# EMA Hourly Continuation — SUPER/USDT P55_89

**Symbol:** SUPER/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.5030 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.9682 |
| sortino_ratio | -1.7608 |
| max_drawdown | 0.8814 |
| cagr | -0.5696 |
| net_avg_win | 30.1741 |
| net_avg_loss | -53.1461 |
| avg_hold_time_bars | 4.9252 |
| exposure | 0.1406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
