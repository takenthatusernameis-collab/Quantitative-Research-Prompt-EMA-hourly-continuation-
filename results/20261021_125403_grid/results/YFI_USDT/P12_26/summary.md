# EMA Hourly Continuation — YFI/USDT P12_26

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.5372 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9253 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -4.7526 |
| sortino_ratio | -1.6870 |
| max_drawdown | 0.8631 |
| cagr | -0.5390 |
| net_avg_win | 34.3499 |
| net_avg_loss | -58.3135 |
| avg_hold_time_bars | 5.3717 |
| exposure | 0.1478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
