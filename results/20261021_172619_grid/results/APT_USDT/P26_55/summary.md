# EMA Hourly Continuation — APT/USDT P26_55

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7274 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9706 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.9236 |
| sortino_ratio | -0.5579 |
| max_drawdown | 0.5022 |
| cagr | -0.2259 |
| net_avg_win | 62.3416 |
| net_avg_loss | -84.4612 |
| avg_hold_time_bars | 7.1540 |
| exposure | 0.1330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
