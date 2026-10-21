# EMA Hourly Continuation — WOO/USDT P12_20

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7501 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0710 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -2.0693 |
| sortino_ratio | -0.5976 |
| max_drawdown | 0.5426 |
| cagr | -0.2397 |
| net_avg_win | 72.8432 |
| net_avg_loss | -100.5430 |
| avg_hold_time_bars | 4.6427 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
