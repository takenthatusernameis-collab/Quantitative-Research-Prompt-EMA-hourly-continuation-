# EMA Hourly Continuation — GTC/USDT P50_100

**Symbol:** GTC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.3828 |
| sortino_ratio | -0.6989 |
| max_drawdown | 0.5738 |
| cagr | -0.2752 |
| net_avg_win | 64.8108 |
| net_avg_loss | -84.9997 |
| avg_hold_time_bars | 9.2908 |
| exposure | 0.1786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
