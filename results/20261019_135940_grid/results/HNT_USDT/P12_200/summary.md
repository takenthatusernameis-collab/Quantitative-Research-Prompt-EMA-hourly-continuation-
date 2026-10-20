# EMA Hourly Continuation — HNT/USDT P12_200

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6741 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -2.3990 |
| sortino_ratio | -0.6854 |
| max_drawdown | 0.5733 |
| cagr | -0.2749 |
| net_avg_win | 59.3745 |
| net_avg_loss | -79.4314 |
| avg_hold_time_bars | 39.5995 |
| exposure | 0.7326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
