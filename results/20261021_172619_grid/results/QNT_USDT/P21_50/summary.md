# EMA Hourly Continuation — QNT/USDT P21_50

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7105 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -2.2845 |
| sortino_ratio | -0.7303 |
| max_drawdown | 0.5858 |
| cagr | -0.2826 |
| net_avg_win | 55.3081 |
| net_avg_loss | -80.7438 |
| avg_hold_time_bars | 6.6369 |
| exposure | 0.1487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
