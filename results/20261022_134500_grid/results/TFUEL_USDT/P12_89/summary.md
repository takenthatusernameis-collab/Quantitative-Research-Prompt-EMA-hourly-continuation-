# EMA Hourly Continuation — TFUEL/USDT P12_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.4927 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.7668 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -7.3617 |
| sortino_ratio | -3.1717 |
| max_drawdown | 0.9808 |
| cagr | -0.7889 |
| net_avg_win | 23.6254 |
| net_avg_loss | -35.1335 |
| avg_hold_time_bars | 11.2991 |
| exposure | 0.4873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
