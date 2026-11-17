# EMA Hourly Continuation — NUM/USDT P12_50

**Symbol:** NUM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.4376 |
| net_win_rate | 0.3736 |
| gross_profit_factor | 0.7782 |
| gross_win_rate | 0.3861 |
| sharpe_ratio | -9.6251 |
| sortino_ratio | -4.3446 |
| max_drawdown | 0.9956 |
| cagr | -0.8836 |
| net_avg_win | 20.0184 |
| net_avg_loss | -27.2758 |
| avg_hold_time_bars | 7.6737 |
| exposure | 0.3614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
