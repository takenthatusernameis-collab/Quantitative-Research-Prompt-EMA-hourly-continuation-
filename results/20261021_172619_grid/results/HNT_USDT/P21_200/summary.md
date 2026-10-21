# EMA Hourly Continuation — HNT/USDT P21_200

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7705 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.2859 |
| sortino_ratio | -0.3028 |
| max_drawdown | 0.3267 |
| cagr | -0.1313 |
| net_avg_win | 76.8741 |
| net_avg_loss | -90.0718 |
| avg_hold_time_bars | 52.3796 |
| exposure | 0.6524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
