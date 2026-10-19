# EMA Hourly Continuation — TRX/USDT P21_50

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 835 |
| net_profit_factor | 0.2044 |
| net_win_rate | 0.3533 |
| gross_profit_factor | 0.8897 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -13.2859 |
| sortino_ratio | -5.7434 |
| max_drawdown | 0.9997 |
| cagr | -0.9581 |
| net_avg_win | 8.7082 |
| net_avg_loss | -23.2693 |
| avg_hold_time_bars | 4.8778 |
| exposure | 0.1851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
