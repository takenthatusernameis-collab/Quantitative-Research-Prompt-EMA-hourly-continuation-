# EMA Hourly Continuation — CARV/USDT P8_20

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.5122 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 1.0350 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -10.1087 |
| sortino_ratio | -5.4726 |
| max_drawdown | 0.9962 |
| cagr | -0.9348 |
| net_avg_win | 19.5851 |
| net_avg_loss | -31.0793 |
| avg_hold_time_bars | 3.8321 |
| exposure | 0.2568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
