# EMA Hourly Continuation — G/USDT P50_55

**Symbol:** G/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.6130 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0110 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -2.2512 |
| sortino_ratio | -0.5020 |
| max_drawdown | 0.3902 |
| cagr | -0.2037 |
| net_avg_win | 59.4304 |
| net_avg_loss | -98.8503 |
| avg_hold_time_bars | 5.0680 |
| exposure | 0.0549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
