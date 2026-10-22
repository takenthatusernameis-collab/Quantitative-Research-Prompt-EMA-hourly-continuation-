# EMA Hourly Continuation — FLR/USDT P12_26

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1612 |
| net_profit_factor | 0.3289 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.7889 |
| gross_win_rate | 0.4150 |
| sharpe_ratio | -15.1363 |
| sortino_ratio | -8.7075 |
| max_drawdown | 1.0000 |
| cagr | -0.9889 |
| net_avg_win | 7.9931 |
| net_avg_loss | -14.9145 |
| avg_hold_time_bars | 2.7742 |
| exposure | 0.2033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
