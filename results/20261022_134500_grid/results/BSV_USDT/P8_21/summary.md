# EMA Hourly Continuation — BSV/USDT P8_21

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1781 |
| net_profit_factor | 0.3001 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.8067 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -15.1143 |
| sortino_ratio | -9.1088 |
| max_drawdown | 1.0000 |
| cagr | -0.9906 |
| net_avg_win | 6.1968 |
| net_avg_loss | -13.1204 |
| avg_hold_time_bars | 2.9540 |
| exposure | 0.2391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
