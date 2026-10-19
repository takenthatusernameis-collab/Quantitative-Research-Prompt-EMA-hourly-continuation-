# EMA Hourly Continuation — JST/USDT P34_55

**Symbol:** JST/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.2124 |
| net_win_rate | 0.3860 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -10.6704 |
| sortino_ratio | -4.2423 |
| max_drawdown | 0.9965 |
| cagr | -0.8940 |
| net_avg_win | 9.3974 |
| net_avg_loss | -27.8085 |
| avg_hold_time_bars | 4.0418 |
| exposure | 0.1355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
