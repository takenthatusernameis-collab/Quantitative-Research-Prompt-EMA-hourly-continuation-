# EMA Hourly Continuation — RPL/USDT P12_26

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1251 |
| net_profit_factor | 0.4559 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.9182 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -8.4892 |
| sortino_ratio | -4.2381 |
| max_drawdown | 0.9945 |
| cagr | -0.8733 |
| net_avg_win | 14.8788 |
| net_avg_loss | -26.4508 |
| avg_hold_time_bars | 3.8577 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
