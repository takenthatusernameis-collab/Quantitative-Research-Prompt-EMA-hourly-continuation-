# EMA Hourly Continuation — XNO/USDT P12_50

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.6183 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.7998 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -4.3974 |
| sortino_ratio | -1.6223 |
| max_drawdown | 0.8588 |
| cagr | -0.5270 |
| net_avg_win | 47.0039 |
| net_avg_loss | -57.6615 |
| avg_hold_time_bars | 8.8508 |
| exposure | 0.2724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
