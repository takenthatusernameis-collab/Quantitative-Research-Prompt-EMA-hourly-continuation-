# EMA Hourly Continuation — BRETT/USDT P26_100

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.6185 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8420 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -3.9241 |
| sortino_ratio | -1.3683 |
| max_drawdown | 0.7874 |
| cagr | -0.4757 |
| net_avg_win | 48.5039 |
| net_avg_loss | -64.4107 |
| avg_hold_time_bars | 13.4355 |
| exposure | 0.3756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
