# EMA Hourly Continuation — MINA/USDT P34_100

**Symbol:** MINA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.9035 |
| net_win_rate | 0.5419 |
| gross_profit_factor | 1.1651 |
| gross_win_rate | 0.5419 |
| sharpe_ratio | -0.5823 |
| sortino_ratio | -0.1745 |
| max_drawdown | 0.3783 |
| cagr | -0.0818 |
| net_avg_win | 77.5633 |
| net_avg_loss | -101.5342 |
| avg_hold_time_bars | 16.3907 |
| exposure | 0.3204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
