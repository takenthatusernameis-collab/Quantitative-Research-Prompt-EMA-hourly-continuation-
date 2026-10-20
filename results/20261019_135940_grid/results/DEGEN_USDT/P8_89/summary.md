# EMA Hourly Continuation — DEGEN/USDT P8_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.7520 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9942 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -2.7696 |
| sortino_ratio | -0.9917 |
| max_drawdown | 0.7004 |
| cagr | -0.3763 |
| net_avg_win | 66.9926 |
| net_avg_loss | -84.5135 |
| avg_hold_time_bars | 22.1953 |
| exposure | 0.6518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
