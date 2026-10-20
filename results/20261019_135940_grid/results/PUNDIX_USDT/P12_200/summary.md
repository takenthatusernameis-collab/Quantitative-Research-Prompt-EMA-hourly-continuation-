# EMA Hourly Continuation — PUNDIX/USDT P12_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7683 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0723 |
| gross_win_rate | 0.5187 |
| sharpe_ratio | -1.4854 |
| sortino_ratio | -0.3951 |
| max_drawdown | 0.3873 |
| cagr | -0.1684 |
| net_avg_win | 69.4294 |
| net_avg_loss | -94.0891 |
| avg_hold_time_bars | 48.9337 |
| exposure | 0.7718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
