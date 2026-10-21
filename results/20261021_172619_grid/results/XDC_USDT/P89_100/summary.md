# EMA Hourly Continuation — XDC/USDT P89_100

**Symbol:** XDC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.5035 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -1.8798 |
| sortino_ratio | -0.2680 |
| max_drawdown | 0.2667 |
| cagr | -0.1145 |
| net_avg_win | 58.0095 |
| net_avg_loss | -101.9105 |
| avg_hold_time_bars | 7.0204 |
| exposure | 0.0313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
