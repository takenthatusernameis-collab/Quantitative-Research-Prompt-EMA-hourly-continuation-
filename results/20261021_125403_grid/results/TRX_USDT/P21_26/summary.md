# EMA Hourly Continuation — TRX/USDT P21_26

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 113 |
| net_profit_factor | 0.3543 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9606 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -3.2540 |
| sortino_ratio | -0.5136 |
| max_drawdown | 0.4567 |
| cagr | -0.2140 |
| net_avg_win | 46.9846 |
| net_avg_loss | -117.1320 |
| avg_hold_time_bars | 8.5044 |
| exposure | 0.0437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
