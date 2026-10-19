# EMA Hourly Continuation — KCS/USDT P8_26

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1508 |
| net_profit_factor | 0.1520 |
| net_win_rate | 0.2951 |
| gross_profit_factor | 0.6203 |
| gross_win_rate | 0.3714 |
| sharpe_ratio | -19.7085 |
| sortino_ratio | -11.4850 |
| max_drawdown | 1.0000 |
| cagr | -0.9983 |
| net_avg_win | 4.0286 |
| net_avg_loss | -11.0938 |
| avg_hold_time_bars | 4.4211 |
| exposure | 0.3030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
