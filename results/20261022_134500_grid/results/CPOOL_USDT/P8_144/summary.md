# EMA Hourly Continuation — CPOOL/USDT P8_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -3.2036 |
| sortino_ratio | -1.1401 |
| max_drawdown | 0.7545 |
| cagr | -0.4206 |
| net_avg_win | 52.5559 |
| net_avg_loss | -68.5761 |
| avg_hold_time_bars | 23.2966 |
| exposure | 0.6820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
