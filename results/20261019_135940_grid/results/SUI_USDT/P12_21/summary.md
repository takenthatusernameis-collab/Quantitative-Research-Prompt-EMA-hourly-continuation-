# EMA Hourly Continuation — SUI/USDT P12_21

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1546 |
| net_profit_factor | 0.3795 |
| net_win_rate | 0.3984 |
| gross_profit_factor | 0.8085 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -13.9341 |
| sortino_ratio | -7.7922 |
| max_drawdown | 1.0000 |
| cagr | -0.9835 |
| net_avg_win | 9.9296 |
| net_avg_loss | -17.3294 |
| avg_hold_time_bars | 2.0336 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
