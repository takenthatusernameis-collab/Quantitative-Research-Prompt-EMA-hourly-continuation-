# EMA Hourly Continuation — CRV/USDT P89_100

**Symbol:** CRV/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 111 |
| net_profit_factor | 0.6648 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.8972 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -1.2779 |
| sortino_ratio | -0.1926 |
| max_drawdown | 0.2214 |
| cagr | -0.0843 |
| net_avg_win | 74.2492 |
| net_avg_loss | -102.0519 |
| avg_hold_time_bars | 4.8108 |
| exposure | 0.0243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
