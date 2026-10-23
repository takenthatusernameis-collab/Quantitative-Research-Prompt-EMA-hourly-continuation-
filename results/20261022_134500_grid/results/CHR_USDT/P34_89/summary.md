# EMA Hourly Continuation — CHR/USDT P34_89

**Symbol:** CHR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.5970 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -4.9943 |
| sortino_ratio | -1.9124 |
| max_drawdown | 0.9041 |
| cagr | -0.6009 |
| net_avg_win | 39.2738 |
| net_avg_loss | -55.5022 |
| avg_hold_time_bars | 7.0283 |
| exposure | 0.2363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
