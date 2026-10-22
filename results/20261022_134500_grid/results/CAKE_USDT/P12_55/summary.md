# EMA Hourly Continuation — CAKE/USDT P12_55

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.5091 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -6.5265 |
| sortino_ratio | -2.7518 |
| max_drawdown | 0.9685 |
| cagr | -0.7433 |
| net_avg_win | 24.1695 |
| net_avg_loss | -39.9626 |
| avg_hold_time_bars | 9.9163 |
| exposure | 0.4093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
