# EMA Hourly Continuation — ACE/USDT P34_144

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7159 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9824 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.2388 |
| sortino_ratio | -0.6433 |
| max_drawdown | 0.5518 |
| cagr | -0.2611 |
| net_avg_win | 67.5895 |
| net_avg_loss | -87.7973 |
| avg_hold_time_bars | 22.5763 |
| exposure | 0.4219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
