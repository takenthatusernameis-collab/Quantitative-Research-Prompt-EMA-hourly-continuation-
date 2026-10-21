# EMA Hourly Continuation — TURBO/USDT P100_144

**Symbol:** TURBO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 212 |
| net_profit_factor | 0.9231 |
| net_win_rate | 0.5519 |
| gross_profit_factor | 1.2188 |
| gross_win_rate | 0.5519 |
| sharpe_ratio | -0.3706 |
| sortino_ratio | -0.0858 |
| max_drawdown | 0.1964 |
| cagr | -0.0416 |
| net_avg_win | 87.2323 |
| net_avg_loss | -116.3814 |
| avg_hold_time_bars | 5.6981 |
| exposure | 0.0659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
