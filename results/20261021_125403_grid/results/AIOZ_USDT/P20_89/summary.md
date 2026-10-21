# EMA Hourly Continuation — AIOZ/USDT P20_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7904 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -1.7409 |
| sortino_ratio | -0.5360 |
| max_drawdown | 0.5027 |
| cagr | -0.2200 |
| net_avg_win | 77.4698 |
| net_avg_loss | -92.2938 |
| avg_hold_time_bars | 17.7597 |
| exposure | 0.3762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
