# EMA Hourly Continuation — WAVES/USDT P26_89

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.5017 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -7.0840 |
| sortino_ratio | -2.8959 |
| max_drawdown | 0.9742 |
| cagr | -0.7605 |
| net_avg_win | 26.9690 |
| net_avg_loss | -40.7381 |
| avg_hold_time_bars | 8.0285 |
| exposure | 0.3073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
