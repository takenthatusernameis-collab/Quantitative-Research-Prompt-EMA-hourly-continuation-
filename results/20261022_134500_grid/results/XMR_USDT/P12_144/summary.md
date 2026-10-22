# EMA Hourly Continuation — XMR/USDT P12_144

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.8414 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -6.0361 |
| sortino_ratio | -2.3538 |
| max_drawdown | 0.9461 |
| cagr | -0.6852 |
| net_avg_win | 27.0879 |
| net_avg_loss | -42.8992 |
| avg_hold_time_bars | 17.2710 |
| exposure | 0.6084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
