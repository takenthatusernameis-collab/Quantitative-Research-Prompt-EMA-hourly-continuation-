# EMA Hourly Continuation — ATOM/USDT P26_55

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6581 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.4586 |
| sortino_ratio | -0.7125 |
| max_drawdown | 0.5686 |
| cagr | -0.2779 |
| net_avg_win | 54.0138 |
| net_avg_loss | -78.1512 |
| avg_hold_time_bars | 7.2794 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
