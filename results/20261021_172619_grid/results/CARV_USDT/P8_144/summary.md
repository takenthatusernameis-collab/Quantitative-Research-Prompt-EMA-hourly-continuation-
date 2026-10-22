# EMA Hourly Continuation — CARV/USDT P8_144

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8295 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0070 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.2579 |
| sortino_ratio | -0.3757 |
| max_drawdown | 0.3855 |
| cagr | -0.1601 |
| net_avg_win | 82.3966 |
| net_avg_loss | -99.3331 |
| avg_hold_time_bars | 34.7045 |
| exposure | 0.6875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
