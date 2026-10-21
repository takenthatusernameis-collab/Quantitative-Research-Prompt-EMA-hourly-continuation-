# EMA Hourly Continuation — FLIP/USDT P89_100

**Symbol:** FLIP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 153 |
| net_profit_factor | 0.3486 |
| net_win_rate | 0.3856 |
| gross_profit_factor | 0.6739 |
| gross_win_rate | 0.3922 |
| sharpe_ratio | -4.0129 |
| sortino_ratio | -0.7041 |
| max_drawdown | 0.5951 |
| cagr | -0.2983 |
| net_avg_win | 53.4418 |
| net_avg_loss | -96.2263 |
| avg_hold_time_bars | 10.8889 |
| exposure | 0.0757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
