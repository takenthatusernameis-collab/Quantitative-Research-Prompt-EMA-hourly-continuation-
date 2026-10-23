# EMA Hourly Continuation — MANTA/USDT P21_34

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.4657 |
| net_win_rate | 0.4203 |
| gross_profit_factor | 0.9782 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -10.1819 |
| sortino_ratio | -4.7871 |
| max_drawdown | 0.9978 |
| cagr | -0.9129 |
| net_avg_win | 18.6210 |
| net_avg_loss | -28.9973 |
| avg_hold_time_bars | 2.7858 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
