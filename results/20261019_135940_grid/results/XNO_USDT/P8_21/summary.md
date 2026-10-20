# EMA Hourly Continuation — XNO/USDT P8_21

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1800 |
| net_profit_factor | 0.2848 |
| net_win_rate | 0.3600 |
| gross_profit_factor | 0.6191 |
| gross_win_rate | 0.3783 |
| sharpe_ratio | -15.6783 |
| sortino_ratio | -9.4419 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 6.1462 |
| net_avg_loss | -12.1377 |
| avg_hold_time_bars | 2.8033 |
| exposure | 0.2294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
