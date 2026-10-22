# EMA Hourly Continuation — LUNA/USDT P12_144

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8218 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0188 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -1.2575 |
| sortino_ratio | -0.3658 |
| max_drawdown | 0.3698 |
| cagr | -0.1565 |
| net_avg_win | 77.1015 |
| net_avg_loss | -95.6629 |
| avg_hold_time_bars | 31.8592 |
| exposure | 0.5966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
