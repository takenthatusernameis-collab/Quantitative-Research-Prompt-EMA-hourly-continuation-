# EMA Hourly Continuation — YFI/USDT P12_200

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8697 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.6990 |
| sortino_ratio | -1.0184 |
| max_drawdown | 0.7366 |
| cagr | -0.3959 |
| net_avg_win | 44.6325 |
| net_avg_loss | -72.0462 |
| avg_hold_time_bars | 42.2494 |
| exposure | 0.7513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
