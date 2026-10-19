# EMA Hourly Continuation — KCS/USDT P8_100

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.3629 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.8060 |
| gross_win_rate | 0.4315 |
| sharpe_ratio | -8.4268 |
| sortino_ratio | -3.0744 |
| max_drawdown | 0.9831 |
| cagr | -0.7981 |
| net_avg_win | 21.3506 |
| net_avg_loss | -37.5952 |
| avg_hold_time_bars | 21.3348 |
| exposure | 0.6517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
