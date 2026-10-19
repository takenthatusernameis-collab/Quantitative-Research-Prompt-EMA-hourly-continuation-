# EMA Hourly Continuation — INJ/USDT P12_50

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.5876 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -6.2491 |
| sortino_ratio | -2.9035 |
| max_drawdown | 0.9718 |
| cagr | -0.7558 |
| net_avg_win | 27.2865 |
| net_avg_loss | -39.9731 |
| avg_hold_time_bars | 7.0420 |
| exposure | 0.3508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
