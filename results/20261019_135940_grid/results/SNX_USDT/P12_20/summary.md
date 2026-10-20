# EMA Hourly Continuation — SNX/USDT P12_20

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1450 |
| net_profit_factor | 0.2965 |
| net_win_rate | 0.4069 |
| gross_profit_factor | 0.8091 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -12.7955 |
| sortino_ratio | -6.9264 |
| max_drawdown | 0.9999 |
| cagr | -0.9709 |
| net_avg_win | 7.1440 |
| net_avg_loss | -16.5275 |
| avg_hold_time_bars | 2.3690 |
| exposure | 0.1554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
