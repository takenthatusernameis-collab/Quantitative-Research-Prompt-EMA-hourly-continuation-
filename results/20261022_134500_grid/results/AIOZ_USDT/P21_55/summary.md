# EMA Hourly Continuation — AIOZ/USDT P21_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.6167 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.9472 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -6.8445 |
| sortino_ratio | -3.0742 |
| max_drawdown | 0.9788 |
| cagr | -0.7773 |
| net_avg_win | 33.8057 |
| net_avg_loss | -45.6800 |
| avg_hold_time_bars | 5.2434 |
| exposure | 0.2438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
