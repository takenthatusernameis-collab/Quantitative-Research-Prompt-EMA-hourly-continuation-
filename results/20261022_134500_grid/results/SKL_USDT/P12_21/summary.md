# EMA Hourly Continuation — SKL/USDT P12_21

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.3552 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.8839 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -12.3179 |
| sortino_ratio | -6.9688 |
| max_drawdown | 0.9999 |
| cagr | -0.9713 |
| net_avg_win | 7.9814 |
| net_avg_loss | -17.0957 |
| avg_hold_time_bars | 2.2511 |
| exposure | 0.1634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
