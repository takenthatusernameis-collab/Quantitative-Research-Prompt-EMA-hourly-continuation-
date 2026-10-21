# EMA Hourly Continuation — KMNO/USDT P12_50

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.7420 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.3257 |
| sortino_ratio | -0.8123 |
| max_drawdown | 0.6295 |
| cagr | -0.3129 |
| net_avg_win | 60.3688 |
| net_avg_loss | -77.5888 |
| avg_hold_time_bars | 11.9390 |
| exposure | 0.3252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
