# EMA Hourly Continuation — DIA/USDT P8_12

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1712 |
| net_profit_factor | 0.1548 |
| net_win_rate | 0.3738 |
| gross_profit_factor | 0.5412 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -16.1278 |
| sortino_ratio | -9.5690 |
| max_drawdown | 1.0000 |
| cagr | -0.9933 |
| net_avg_win | 2.8607 |
| net_avg_loss | -11.0362 |
| avg_hold_time_bars | 2.2576 |
| exposure | 0.1749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
