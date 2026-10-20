# EMA Hourly Continuation — BICO/USDT P21_89

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.6046 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -4.4802 |
| sortino_ratio | -1.6531 |
| max_drawdown | 0.8665 |
| cagr | -0.5395 |
| net_avg_win | 42.9801 |
| net_avg_loss | -57.5134 |
| avg_hold_time_bars | 12.9531 |
| exposure | 0.4015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
