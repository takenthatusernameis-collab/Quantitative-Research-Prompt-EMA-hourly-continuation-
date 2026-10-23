# EMA Hourly Continuation — OSMO/USDT P8_89

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 1.0323 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -3.7748 |
| sortino_ratio | -1.4020 |
| max_drawdown | 0.8314 |
| cagr | -0.4931 |
| net_avg_win | 53.0175 |
| net_avg_loss | -71.4682 |
| avg_hold_time_bars | 20.5021 |
| exposure | 0.6570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
