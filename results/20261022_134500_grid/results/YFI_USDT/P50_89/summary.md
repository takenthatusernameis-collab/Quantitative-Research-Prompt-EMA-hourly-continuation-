# EMA Hourly Continuation — YFI/USDT P50_89

**Symbol:** YFI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.4298 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 1.0223 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -8.2250 |
| sortino_ratio | -3.2746 |
| max_drawdown | 0.9855 |
| cagr | -0.8072 |
| net_avg_win | 21.8856 |
| net_avg_loss | -38.6176 |
| avg_hold_time_bars | 4.6018 |
| exposure | 0.1637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
