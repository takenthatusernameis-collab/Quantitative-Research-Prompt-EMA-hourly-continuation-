# EMA Hourly Continuation — WIF/USDT P8_200

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6360 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8555 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -2.6842 |
| sortino_ratio | -0.7488 |
| max_drawdown | 0.5982 |
| cagr | -0.2956 |
| net_avg_win | 56.5027 |
| net_avg_loss | -76.5680 |
| avg_hold_time_bars | 44.6777 |
| exposure | 0.7940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
