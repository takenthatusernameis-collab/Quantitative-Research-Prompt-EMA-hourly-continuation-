# EMA Hourly Continuation — ILV/USDT P20_55

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.7525 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9990 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -2.2562 |
| sortino_ratio | -0.7723 |
| max_drawdown | 0.6116 |
| cagr | -0.2975 |
| net_avg_win | 62.9494 |
| net_avg_loss | -83.0695 |
| avg_hold_time_bars | 7.6175 |
| exposure | 0.1974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
