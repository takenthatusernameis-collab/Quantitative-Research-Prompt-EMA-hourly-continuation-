# EMA Hourly Continuation — WIF/USDT P8_26

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1562 |
| net_profit_factor | 0.6055 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.9456 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -8.5601 |
| sortino_ratio | -4.7424 |
| max_drawdown | 0.9972 |
| cagr | -0.9031 |
| net_avg_win | 21.6442 |
| net_avg_loss | -29.5602 |
| avg_hold_time_bars | 3.6204 |
| exposure | 0.2570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
