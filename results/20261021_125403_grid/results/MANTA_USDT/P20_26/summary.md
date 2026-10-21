# EMA Hourly Continuation — MANTA/USDT P20_26

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5690 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -2.9636 |
| sortino_ratio | -0.6745 |
| max_drawdown | 0.5779 |
| cagr | -0.2671 |
| net_avg_win | 63.2850 |
| net_avg_loss | -89.1403 |
| avg_hold_time_bars | 5.0827 |
| exposure | 0.0587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
