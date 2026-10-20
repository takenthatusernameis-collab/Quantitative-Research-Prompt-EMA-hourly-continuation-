# EMA Hourly Continuation — NOT/USDT P20_89

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.5962 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -4.6576 |
| sortino_ratio | -1.7981 |
| max_drawdown | 0.8885 |
| cagr | -0.5854 |
| net_avg_win | 37.4312 |
| net_avg_loss | -55.8804 |
| avg_hold_time_bars | 10.6022 |
| exposure | 0.3680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
