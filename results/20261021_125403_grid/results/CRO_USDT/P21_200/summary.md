# EMA Hourly Continuation — CRO/USDT P21_200

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0105 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.0856 |
| sortino_ratio | -0.2438 |
| max_drawdown | 0.2957 |
| cagr | -0.1062 |
| net_avg_win | 68.6400 |
| net_avg_loss | -91.9674 |
| avg_hold_time_bars | 61.3796 |
| exposure | 0.6835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
