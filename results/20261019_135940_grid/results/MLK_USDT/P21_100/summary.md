# EMA Hourly Continuation — MLK/USDT P21_100

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.3303 |
| net_win_rate | 0.2946 |
| gross_profit_factor | 0.5622 |
| gross_win_rate | 0.3048 |
| sharpe_ratio | -12.3900 |
| sortino_ratio | -5.5060 |
| max_drawdown | 0.9991 |
| cagr | -0.9364 |
| net_avg_win | 17.0465 |
| net_avg_loss | -21.5561 |
| avg_hold_time_bars | 8.6086 |
| exposure | 0.3822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
