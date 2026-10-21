# EMA Hourly Continuation — SUI/USDT P8_34

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.8217 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.7569 |
| sortino_ratio | -0.6460 |
| max_drawdown | 0.5663 |
| cagr | -0.2586 |
| net_avg_win | 72.8822 |
| net_avg_loss | -92.0061 |
| avg_hold_time_bars | 9.1860 |
| exposure | 0.2739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
