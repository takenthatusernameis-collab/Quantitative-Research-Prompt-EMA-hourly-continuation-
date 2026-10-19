# EMA Hourly Continuation — JTO/USDT P55_200

**Symbol:** JTO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6426 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8634 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -2.7791 |
| sortino_ratio | -0.7990 |
| max_drawdown | 0.6248 |
| cagr | -0.3094 |
| net_avg_win | 57.5974 |
| net_avg_loss | -75.6238 |
| avg_hold_time_bars | 18.0993 |
| exposure | 0.3398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
