# EMA Hourly Continuation — CHR/USDT P50_89

**Symbol:** CHR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6461 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8486 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -2.7998 |
| sortino_ratio | -0.8321 |
| max_drawdown | 0.6503 |
| cagr | -0.3172 |
| net_avg_win | 55.8428 |
| net_avg_loss | -74.2987 |
| avg_hold_time_bars | 6.8169 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
