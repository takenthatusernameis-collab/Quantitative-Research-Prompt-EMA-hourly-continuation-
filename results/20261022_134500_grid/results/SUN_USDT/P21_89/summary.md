# EMA Hourly Continuation — SUN/USDT P21_89

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.3731 |
| net_win_rate | 0.3808 |
| gross_profit_factor | 0.7772 |
| gross_win_rate | 0.4350 |
| sharpe_ratio | -8.3288 |
| sortino_ratio | -2.9799 |
| max_drawdown | 0.9792 |
| cagr | -0.7836 |
| net_avg_win | 23.6865 |
| net_avg_loss | -39.0411 |
| avg_hold_time_bars | 13.6625 |
| exposure | 0.3994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
