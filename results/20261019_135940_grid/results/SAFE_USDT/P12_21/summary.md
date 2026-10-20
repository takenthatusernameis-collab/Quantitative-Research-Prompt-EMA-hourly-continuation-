# EMA Hourly Continuation — SAFE/USDT P12_21

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1350 |
| net_profit_factor | 0.2841 |
| net_win_rate | 0.4074 |
| gross_profit_factor | 0.7273 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -12.0256 |
| sortino_ratio | -6.2941 |
| max_drawdown | 0.9997 |
| cagr | -0.9594 |
| net_avg_win | 7.2139 |
| net_avg_loss | -17.4553 |
| avg_hold_time_bars | 3.2163 |
| exposure | 0.1988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
