# EMA Hourly Continuation — 1INCH/USDT P55_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.4137 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -7.7296 |
| sortino_ratio | -2.9064 |
| max_drawdown | 0.9761 |
| cagr | -0.7722 |
| net_avg_win | 22.5740 |
| net_avg_loss | -41.3965 |
| avg_hold_time_bars | 4.0820 |
| exposure | 0.1312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
