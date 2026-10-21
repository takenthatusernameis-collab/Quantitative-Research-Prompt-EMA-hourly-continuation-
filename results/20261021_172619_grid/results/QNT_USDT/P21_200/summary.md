# EMA Hourly Continuation — QNT/USDT P21_200

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7958 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.3991 |
| sortino_ratio | -0.3854 |
| max_drawdown | 0.4124 |
| cagr | -0.1628 |
| net_avg_win | 76.2494 |
| net_avg_loss | -94.7822 |
| avg_hold_time_bars | 35.6000 |
| exposure | 0.5987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
