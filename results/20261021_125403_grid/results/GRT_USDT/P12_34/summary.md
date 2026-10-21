# EMA Hourly Continuation — GRT/USDT P12_34

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8531 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -3.4388 |
| sortino_ratio | -1.1782 |
| max_drawdown | 0.7526 |
| cagr | -0.4171 |
| net_avg_win | 49.9478 |
| net_avg_loss | -66.3672 |
| avg_hold_time_bars | 6.8379 |
| exposure | 0.1795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
