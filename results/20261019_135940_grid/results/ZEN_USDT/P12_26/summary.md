# EMA Hourly Continuation — ZEN/USDT P12_26

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1458 |
| net_profit_factor | 0.3609 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.8212 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -11.2030 |
| sortino_ratio | -6.0490 |
| max_drawdown | 0.9995 |
| cagr | -0.9512 |
| net_avg_win | 9.2378 |
| net_avg_loss | -18.4642 |
| avg_hold_time_bars | 2.9671 |
| exposure | 0.1966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
