# EMA Hourly Continuation — XMR/USDT P100_200

**Symbol:** XMR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.3628 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7885 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -7.7219 |
| sortino_ratio | -2.7820 |
| max_drawdown | 0.9747 |
| cagr | -0.7674 |
| net_avg_win | 19.9543 |
| net_avg_loss | -40.0275 |
| avg_hold_time_bars | 5.5879 |
| exposure | 0.1676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
