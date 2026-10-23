# EMA Hourly Continuation — MASK/USDT P26_55

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.4005 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8627 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -7.9041 |
| sortino_ratio | -3.4197 |
| max_drawdown | 0.9868 |
| cagr | -0.8187 |
| net_avg_win | 15.6102 |
| net_avg_loss | -31.7572 |
| avg_hold_time_bars | 4.4404 |
| exposure | 0.1897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
