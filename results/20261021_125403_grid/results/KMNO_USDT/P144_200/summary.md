# EMA Hourly Continuation — KMNO/USDT P144_200

**Symbol:** KMNO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.8359 |
| net_win_rate | 0.5330 |
| gross_profit_factor | 1.1366 |
| gross_win_rate | 0.5330 |
| sharpe_ratio | -0.8006 |
| sortino_ratio | -0.1629 |
| max_drawdown | 0.2452 |
| cagr | -0.0740 |
| net_avg_win | 83.9240 |
| net_avg_loss | -114.5931 |
| avg_hold_time_bars | 7.1523 |
| exposure | 0.0651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
