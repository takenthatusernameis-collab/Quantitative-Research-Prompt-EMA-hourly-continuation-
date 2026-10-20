# EMA Hourly Continuation — HNT/USDT P8_26

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1527 |
| net_profit_factor | 0.3946 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.7133 |
| gross_win_rate | 0.4158 |
| sharpe_ratio | -11.2015 |
| sortino_ratio | -6.1611 |
| max_drawdown | 0.9995 |
| cagr | -0.9530 |
| net_avg_win | 10.5932 |
| net_avg_loss | -18.1033 |
| avg_hold_time_bars | 4.3779 |
| exposure | 0.3039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
