# EMA Hourly Continuation — OP/USDT P8_50

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.5227 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8950 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -6.3685 |
| sortino_ratio | -2.8977 |
| max_drawdown | 0.9719 |
| cagr | -0.7546 |
| net_avg_win | 22.1017 |
| net_avg_loss | -35.7424 |
| avg_hold_time_bars | 10.1143 |
| exposure | 0.4827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
