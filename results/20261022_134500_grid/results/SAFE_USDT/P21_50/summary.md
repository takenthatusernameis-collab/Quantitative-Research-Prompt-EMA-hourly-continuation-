# EMA Hourly Continuation — SAFE/USDT P21_50

**Symbol:** SAFE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.5288 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -5.8747 |
| sortino_ratio | -2.5423 |
| max_drawdown | 0.9546 |
| cagr | -0.7074 |
| net_avg_win | 23.9877 |
| net_avg_loss | -40.9537 |
| avg_hold_time_bars | 5.2085 |
| exposure | 0.2242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
