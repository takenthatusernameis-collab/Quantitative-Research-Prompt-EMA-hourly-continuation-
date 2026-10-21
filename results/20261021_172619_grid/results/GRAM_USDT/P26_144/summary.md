# EMA Hourly Continuation — GRAM/USDT P26_144

**Symbol:** GRAM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.8805 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -2.2678 |
| sortino_ratio | -0.6277 |
| max_drawdown | 0.5440 |
| cagr | -0.2502 |
| net_avg_win | 60.2873 |
| net_avg_loss | -80.0967 |
| avg_hold_time_bars | 24.9815 |
| exposure | 0.4292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
