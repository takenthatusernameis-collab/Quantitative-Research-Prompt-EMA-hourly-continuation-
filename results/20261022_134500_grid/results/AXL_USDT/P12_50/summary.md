# EMA Hourly Continuation — AXL/USDT P12_50

**Symbol:** AXL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.6239 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.9554 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -6.8416 |
| sortino_ratio | -3.2654 |
| max_drawdown | 0.9803 |
| cagr | -0.7872 |
| net_avg_win | 32.0007 |
| net_avg_loss | -40.7103 |
| avg_hold_time_bars | 6.7700 |
| exposure | 0.3517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
