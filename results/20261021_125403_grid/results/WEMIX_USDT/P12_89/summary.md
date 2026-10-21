# EMA Hourly Continuation — WEMIX/USDT P12_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.5167 |
| net_win_rate | 0.3824 |
| gross_profit_factor | 0.6496 |
| gross_win_rate | 0.3824 |
| sharpe_ratio | -4.9692 |
| sortino_ratio | -1.5490 |
| max_drawdown | 0.8392 |
| cagr | -0.5134 |
| net_avg_win | 47.8132 |
| net_avg_loss | -57.2947 |
| avg_hold_time_bars | 22.5133 |
| exposure | 0.5004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
