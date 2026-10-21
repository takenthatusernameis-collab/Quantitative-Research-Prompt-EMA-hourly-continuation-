# EMA Hourly Continuation — TRX/USDT P34_50

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.3240 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -4.5398 |
| sortino_ratio | -0.9383 |
| max_drawdown | 0.6661 |
| cagr | -0.3539 |
| net_avg_win | 38.0135 |
| net_avg_loss | -90.4046 |
| avg_hold_time_bars | 6.7979 |
| exposure | 0.0596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
