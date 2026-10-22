# EMA Hourly Continuation — SYN/USDT P12_200

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8734 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -0.6846 |
| sortino_ratio | -0.1784 |
| max_drawdown | 0.2638 |
| cagr | -0.0820 |
| net_avg_win | 79.8859 |
| net_avg_loss | -93.1397 |
| avg_hold_time_bars | 48.5801 |
| exposure | 0.7309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
