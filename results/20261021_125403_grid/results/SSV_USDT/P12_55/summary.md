# EMA Hourly Continuation — SSV/USDT P12_55

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.7293 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.9056 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -3.2291 |
| sortino_ratio | -1.1908 |
| max_drawdown | 0.7761 |
| cagr | -0.4227 |
| net_avg_win | 65.1575 |
| net_avg_loss | -75.4702 |
| avg_hold_time_bars | 12.0635 |
| exposure | 0.3696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
