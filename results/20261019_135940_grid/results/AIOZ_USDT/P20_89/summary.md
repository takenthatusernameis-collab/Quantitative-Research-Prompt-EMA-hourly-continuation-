# EMA Hourly Continuation — AIOZ/USDT P20_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.6559 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.9293 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -4.4890 |
| sortino_ratio | -1.7277 |
| max_drawdown | 0.8758 |
| cagr | -0.5620 |
| net_avg_win | 48.0146 |
| net_avg_loss | -63.5082 |
| avg_hold_time_bars | 11.7015 |
| exposure | 0.3973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
