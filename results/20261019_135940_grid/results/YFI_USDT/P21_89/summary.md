# EMA Hourly Continuation — YFI/USDT P21_89

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 826 |
| net_profit_factor | 0.5162 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.9691 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -7.1908 |
| sortino_ratio | -2.8785 |
| max_drawdown | 0.9756 |
| cagr | -0.7670 |
| net_avg_win | 28.8096 |
| net_avg_loss | -43.3265 |
| avg_hold_time_bars | 9.6453 |
| exposure | 0.3605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
