# EMA Hourly Continuation — ETHFI/USDT P21_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.5974 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.9398 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -6.3910 |
| sortino_ratio | -2.8707 |
| max_drawdown | 0.9718 |
| cagr | -0.7492 |
| net_avg_win | 31.3895 |
| net_avg_loss | -43.1294 |
| avg_hold_time_bars | 5.0256 |
| exposure | 0.2321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
