# EMA Hourly Continuation — DYDX/USDT P34_89

**Symbol:** DYDX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9806 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -4.3624 |
| sortino_ratio | -1.6504 |
| max_drawdown | 0.8712 |
| cagr | -0.5430 |
| net_avg_win | 44.0490 |
| net_avg_loss | -63.9179 |
| avg_hold_time_bars | 7.1586 |
| exposure | 0.2340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
