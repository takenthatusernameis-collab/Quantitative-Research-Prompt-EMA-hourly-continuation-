# EMA Hourly Continuation — DASH/USDT P26_89

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7856 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0433 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.5837 |
| sortino_ratio | -0.4753 |
| max_drawdown | 0.4937 |
| cagr | -0.1964 |
| net_avg_win | 69.7548 |
| net_avg_loss | -91.6789 |
| avg_hold_time_bars | 14.3181 |
| exposure | 0.2844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
