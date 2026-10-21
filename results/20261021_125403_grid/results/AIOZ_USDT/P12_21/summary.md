# EMA Hourly Continuation — AIOZ/USDT P12_21

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.5437 |
| net_win_rate | 0.4021 |
| gross_profit_factor | 0.7097 |
| gross_win_rate | 0.4021 |
| sharpe_ratio | -3.5259 |
| sortino_ratio | -0.8443 |
| max_drawdown | 0.6357 |
| cagr | -0.3233 |
| net_avg_win | 64.7396 |
| net_avg_loss | -80.0824 |
| avg_hold_time_bars | 5.6434 |
| exposure | 0.0734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
