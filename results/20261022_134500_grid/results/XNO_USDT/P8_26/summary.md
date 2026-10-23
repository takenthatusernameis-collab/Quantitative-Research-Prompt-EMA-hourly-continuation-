# EMA Hourly Continuation — XNO/USDT P8_26

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1692 |
| net_profit_factor | 0.3463 |
| net_win_rate | 0.3753 |
| gross_profit_factor | 0.7022 |
| gross_win_rate | 0.3936 |
| sharpe_ratio | -13.6904 |
| sortino_ratio | -7.9766 |
| max_drawdown | 1.0000 |
| cagr | -0.9815 |
| net_avg_win | 8.3419 |
| net_avg_loss | -14.4718 |
| avg_hold_time_bars | 3.4645 |
| exposure | 0.2665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
