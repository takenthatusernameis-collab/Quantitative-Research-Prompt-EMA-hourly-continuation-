# EMA Hourly Continuation — RUNE/USDT P21_50

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.5228 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9216 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -6.6569 |
| sortino_ratio | -2.9577 |
| max_drawdown | 0.9720 |
| cagr | -0.7584 |
| net_avg_win | 22.8908 |
| net_avg_loss | -39.3844 |
| avg_hold_time_bars | 4.5509 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
