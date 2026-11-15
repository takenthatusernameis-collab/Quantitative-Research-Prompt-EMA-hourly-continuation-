# EMA Hourly Continuation — CERE/USDT P26_200

**Symbol:** CERE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.5511 |
| net_win_rate | 0.3874 |
| gross_profit_factor | 0.8048 |
| gross_win_rate | 0.3979 |
| sharpe_ratio | -5.9895 |
| sortino_ratio | -1.8272 |
| max_drawdown | 0.9087 |
| cagr | -0.6040 |
| net_avg_win | 60.2049 |
| net_avg_loss | -69.0752 |
| avg_hold_time_bars | 25.4421 |
| exposure | 0.5493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
