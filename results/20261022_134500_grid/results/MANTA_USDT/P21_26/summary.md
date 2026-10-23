# EMA Hourly Continuation — MANTA/USDT P21_26

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1146 |
| net_profit_factor | 0.3080 |
| net_win_rate | 0.3743 |
| gross_profit_factor | 0.8757 |
| gross_win_rate | 0.4215 |
| sharpe_ratio | -13.1496 |
| sortino_ratio | -6.4029 |
| max_drawdown | 0.9998 |
| cagr | -0.9670 |
| net_avg_win | 10.3723 |
| net_avg_loss | -20.1504 |
| avg_hold_time_bars | 2.2199 |
| exposure | 0.1156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
