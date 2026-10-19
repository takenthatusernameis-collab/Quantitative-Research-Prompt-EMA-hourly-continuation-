# EMA Hourly Continuation — ZRO/USDT P12_34

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1210 |
| net_profit_factor | 0.5858 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9646 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -6.8596 |
| sortino_ratio | -3.4816 |
| max_drawdown | 0.9813 |
| cagr | -0.8172 |
| net_avg_win | 24.1677 |
| net_avg_loss | -37.2364 |
| avg_hold_time_bars | 4.0182 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
