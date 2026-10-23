# EMA Hourly Continuation — GMX/USDT P20_21

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.1112 |
| net_win_rate | 0.3049 |
| gross_profit_factor | 0.6389 |
| gross_win_rate | 0.3961 |
| sharpe_ratio | -16.6694 |
| sortino_ratio | -8.5746 |
| max_drawdown | 1.0000 |
| cagr | -0.9908 |
| net_avg_win | 3.4666 |
| net_avg_loss | -13.6712 |
| avg_hold_time_bars | 2.3927 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
