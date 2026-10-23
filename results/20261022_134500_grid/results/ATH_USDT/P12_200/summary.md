# EMA Hourly Continuation — ATH/USDT P12_200

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8540 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1216 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.7916 |
| sortino_ratio | -0.1953 |
| max_drawdown | 0.2378 |
| cagr | -0.0921 |
| net_avg_win | 77.7999 |
| net_avg_loss | -104.0201 |
| avg_hold_time_bars | 56.0697 |
| exposure | 0.7800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
