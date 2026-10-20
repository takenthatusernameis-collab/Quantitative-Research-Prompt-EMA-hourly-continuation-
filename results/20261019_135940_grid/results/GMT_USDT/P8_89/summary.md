# EMA Hourly Continuation — GMT/USDT P8_89

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.5991 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9131 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -4.2167 |
| sortino_ratio | -1.5600 |
| max_drawdown | 0.8578 |
| cagr | -0.5272 |
| net_avg_win | 38.9722 |
| net_avg_loss | -57.4507 |
| avg_hold_time_bars | 20.7374 |
| exposure | 0.6532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
