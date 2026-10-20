# EMA Hourly Continuation — MLK/USDT P21_55

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1243 |
| net_profit_factor | 0.2606 |
| net_win_rate | 0.2776 |
| gross_profit_factor | 0.5703 |
| gross_win_rate | 0.2936 |
| sharpe_ratio | -15.8820 |
| sortino_ratio | -8.0920 |
| max_drawdown | 1.0000 |
| cagr | -0.9842 |
| net_avg_win | 10.2179 |
| net_avg_loss | -15.0611 |
| avg_hold_time_bars | 4.2759 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
