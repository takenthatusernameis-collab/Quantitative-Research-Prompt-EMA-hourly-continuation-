# EMA Hourly Continuation — XYO/USDT P12_21

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1583 |
| net_profit_factor | 0.2526 |
| net_win_rate | 0.3588 |
| gross_profit_factor | 0.7790 |
| gross_win_rate | 0.3955 |
| sharpe_ratio | -16.1904 |
| sortino_ratio | -9.2911 |
| max_drawdown | 1.0000 |
| cagr | -0.9922 |
| net_avg_win | 5.9497 |
| net_avg_loss | -13.1816 |
| avg_hold_time_bars | 2.5995 |
| exposure | 0.1862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
