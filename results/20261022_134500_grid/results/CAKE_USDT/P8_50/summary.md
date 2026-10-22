# EMA Hourly Continuation — CAKE/USDT P8_50

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.5062 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9520 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -6.4676 |
| sortino_ratio | -2.8837 |
| max_drawdown | 0.9719 |
| cagr | -0.7584 |
| net_avg_win | 20.8818 |
| net_avg_loss | -36.7816 |
| avg_hold_time_bars | 10.7164 |
| exposure | 0.4930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
