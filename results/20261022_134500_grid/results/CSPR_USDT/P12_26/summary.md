# EMA Hourly Continuation — CSPR/USDT P12_26

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1630 |
| net_profit_factor | 0.2851 |
| net_win_rate | 0.3724 |
| gross_profit_factor | 0.7477 |
| gross_win_rate | 0.3963 |
| sharpe_ratio | -14.2467 |
| sortino_ratio | -8.1771 |
| max_drawdown | 1.0000 |
| cagr | -0.9843 |
| net_avg_win | 6.5696 |
| net_avg_loss | -13.6730 |
| avg_hold_time_bars | 2.6362 |
| exposure | 0.1953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
