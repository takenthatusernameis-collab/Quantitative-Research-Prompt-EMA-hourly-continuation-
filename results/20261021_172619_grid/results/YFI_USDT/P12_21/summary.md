# EMA Hourly Continuation — YFI/USDT P12_21

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.4258 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.7558 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -5.2828 |
| sortino_ratio | -1.6130 |
| max_drawdown | 0.8544 |
| cagr | -0.5254 |
| net_avg_win | 32.0595 |
| net_avg_loss | -58.3303 |
| avg_hold_time_bars | 5.2539 |
| exposure | 0.1067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
