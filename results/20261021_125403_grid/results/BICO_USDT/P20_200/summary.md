# EMA Hourly Continuation — BICO/USDT P20_200

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.7597 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -1.4914 |
| sortino_ratio | -0.3605 |
| max_drawdown | 0.3921 |
| cagr | -0.1539 |
| net_avg_win | 79.6708 |
| net_avg_loss | -92.0125 |
| avg_hold_time_bars | 48.6460 |
| exposure | 0.6435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
