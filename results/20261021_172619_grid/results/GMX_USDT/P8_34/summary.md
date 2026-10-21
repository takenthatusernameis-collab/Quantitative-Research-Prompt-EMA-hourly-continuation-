# EMA Hourly Continuation — GMX/USDT P8_34

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.6758 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.7772 |
| sortino_ratio | -1.5246 |
| max_drawdown | 0.8266 |
| cagr | -0.5017 |
| net_avg_win | 45.6788 |
| net_avg_loss | -60.0990 |
| avg_hold_time_bars | 9.0262 |
| exposure | 0.3286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
