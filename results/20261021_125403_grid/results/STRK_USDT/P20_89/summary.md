# EMA Hourly Continuation — STRK/USDT P20_89

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7998 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9766 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -1.5788 |
| sortino_ratio | -0.5045 |
| max_drawdown | 0.4820 |
| cagr | -0.2082 |
| net_avg_win | 71.7572 |
| net_avg_loss | -87.9349 |
| avg_hold_time_bars | 15.7255 |
| exposure | 0.3567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
