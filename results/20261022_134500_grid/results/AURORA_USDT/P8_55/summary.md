# EMA Hourly Continuation — AURORA/USDT P8_55

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.5296 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.8718 |
| gross_win_rate | 0.4287 |
| sharpe_ratio | -7.8236 |
| sortino_ratio | -3.4074 |
| max_drawdown | 0.9858 |
| cagr | -0.8140 |
| net_avg_win | 27.6629 |
| net_avg_loss | -37.4045 |
| avg_hold_time_bars | 10.8616 |
| exposure | 0.4745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
