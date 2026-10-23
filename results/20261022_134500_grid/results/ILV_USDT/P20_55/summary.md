# EMA Hourly Continuation — ILV/USDT P20_55

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.5707 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.9310 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -6.2427 |
| sortino_ratio | -2.7161 |
| max_drawdown | 0.9651 |
| cagr | -0.7295 |
| net_avg_win | 29.2763 |
| net_avg_loss | -43.7015 |
| avg_hold_time_bars | 5.3221 |
| exposure | 0.2298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
