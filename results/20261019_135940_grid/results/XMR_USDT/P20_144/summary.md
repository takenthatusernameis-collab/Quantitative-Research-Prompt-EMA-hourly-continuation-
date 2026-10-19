# EMA Hourly Continuation — XMR/USDT P20_144

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.4830 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -6.5170 |
| sortino_ratio | -2.5933 |
| max_drawdown | 0.9609 |
| cagr | -0.7236 |
| net_avg_win | 25.3460 |
| net_avg_loss | -40.6494 |
| avg_hold_time_bars | 13.0838 |
| exposure | 0.4823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
