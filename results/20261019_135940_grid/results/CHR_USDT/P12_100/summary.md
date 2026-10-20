# EMA Hourly Continuation — CHR/USDT P12_100

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.6784 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.9783 |
| sortino_ratio | -1.0237 |
| max_drawdown | 0.7200 |
| cagr | -0.3840 |
| net_avg_win | 52.2202 |
| net_avg_loss | -70.7655 |
| avg_hold_time_bars | 23.1025 |
| exposure | 0.6220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
