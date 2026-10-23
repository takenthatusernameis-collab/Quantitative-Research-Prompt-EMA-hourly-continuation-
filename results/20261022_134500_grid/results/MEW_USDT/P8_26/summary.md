# EMA Hourly Continuation — MEW/USDT P8_26

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1494 |
| net_profit_factor | 0.5690 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8910 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -9.3032 |
| sortino_ratio | -5.0608 |
| max_drawdown | 0.9980 |
| cagr | -0.9150 |
| net_avg_win | 20.4592 |
| net_avg_loss | -27.2415 |
| avg_hold_time_bars | 3.9183 |
| exposure | 0.2661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
