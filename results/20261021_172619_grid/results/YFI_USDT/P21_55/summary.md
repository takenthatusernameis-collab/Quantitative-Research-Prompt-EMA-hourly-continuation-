# EMA Hourly Continuation — YFI/USDT P21_55

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -4.1734 |
| sortino_ratio | -1.5038 |
| max_drawdown | 0.8282 |
| cagr | -0.4968 |
| net_avg_win | 44.7917 |
| net_avg_loss | -65.4018 |
| avg_hold_time_bars | 7.1390 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
