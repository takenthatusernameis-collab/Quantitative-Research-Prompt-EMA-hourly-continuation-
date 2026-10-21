# EMA Hourly Continuation — T/USDT P8_144

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.8382 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0766 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -1.0950 |
| sortino_ratio | -0.2997 |
| max_drawdown | 0.3798 |
| cagr | -0.1310 |
| net_avg_win | 81.7280 |
| net_avg_loss | -104.1198 |
| avg_hold_time_bars | 43.0902 |
| exposure | 0.7137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
