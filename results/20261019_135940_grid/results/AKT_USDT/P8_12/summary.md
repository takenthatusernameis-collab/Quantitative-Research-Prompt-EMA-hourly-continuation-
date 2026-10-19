# EMA Hourly Continuation — AKT/USDT P8_12

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1709 |
| net_profit_factor | 0.2783 |
| net_win_rate | 0.3692 |
| gross_profit_factor | 0.8679 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -16.7781 |
| sortino_ratio | -9.9731 |
| max_drawdown | 1.0000 |
| cagr | -0.9953 |
| net_avg_win | 6.1117 |
| net_avg_loss | -12.8539 |
| avg_hold_time_bars | 1.8139 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
