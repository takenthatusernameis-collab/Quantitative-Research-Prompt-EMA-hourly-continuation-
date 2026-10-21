# EMA Hourly Continuation — BDX/USDT P8_100

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.5131 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7679 |
| gross_win_rate | 0.4120 |
| sharpe_ratio | -5.8221 |
| sortino_ratio | -2.0062 |
| max_drawdown | 0.9084 |
| cagr | -0.6091 |
| net_avg_win | 39.9278 |
| net_avg_loss | -53.7500 |
| avg_hold_time_bars | 13.1094 |
| exposure | 0.3486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
