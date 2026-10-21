# EMA Hourly Continuation — KSM/USDT P34_144

**Symbol:** KSM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7927 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0065 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.4182 |
| sortino_ratio | -0.3734 |
| max_drawdown | 0.4375 |
| cagr | -0.1588 |
| net_avg_win | 79.2550 |
| net_avg_loss | -100.5704 |
| avg_hold_time_bars | 28.2035 |
| exposure | 0.4346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
