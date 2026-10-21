# EMA Hourly Continuation — FLR/USDT P12_89

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.7660 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -2.0114 |
| sortino_ratio | -0.7187 |
| max_drawdown | 0.5920 |
| cagr | -0.2820 |
| net_avg_win | 59.2641 |
| net_avg_loss | -77.8665 |
| avg_hold_time_bars | 16.0273 |
| exposure | 0.4531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
