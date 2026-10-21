# EMA Hourly Continuation — JTO/USDT P12_50

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.8554 |
| net_win_rate | 0.5121 |
| gross_profit_factor | 1.0541 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -1.3186 |
| sortino_ratio | -0.4873 |
| max_drawdown | 0.5143 |
| cagr | -0.2044 |
| net_avg_win | 76.2521 |
| net_avg_loss | -93.5551 |
| avg_hold_time_bars | 11.7462 |
| exposure | 0.3535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
