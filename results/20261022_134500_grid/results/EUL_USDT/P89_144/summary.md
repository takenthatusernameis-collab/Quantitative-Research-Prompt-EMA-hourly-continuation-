# EMA Hourly Continuation — EUL/USDT P89_144

**Symbol:** EUL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.3641 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.6215 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -6.0409 |
| sortino_ratio | -1.8146 |
| max_drawdown | 0.8963 |
| cagr | -0.5920 |
| net_avg_win | 28.7789 |
| net_avg_loss | -50.7943 |
| avg_hold_time_bars | 6.0703 |
| exposure | 0.1255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
