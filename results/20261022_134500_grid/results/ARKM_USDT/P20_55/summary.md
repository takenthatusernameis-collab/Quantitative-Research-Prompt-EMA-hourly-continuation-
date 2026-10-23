# EMA Hourly Continuation — ARKM/USDT P20_55

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.6271 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -5.7930 |
| sortino_ratio | -2.5934 |
| max_drawdown | 0.9572 |
| cagr | -0.7094 |
| net_avg_win | 34.3184 |
| net_avg_loss | -47.7841 |
| avg_hold_time_bars | 5.1464 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
