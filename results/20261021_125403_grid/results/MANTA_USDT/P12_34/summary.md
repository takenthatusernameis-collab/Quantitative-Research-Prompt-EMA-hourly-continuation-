# EMA Hourly Continuation — MANTA/USDT P12_34

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.6429 |
| sortino_ratio | -0.9721 |
| max_drawdown | 0.6809 |
| cagr | -0.3598 |
| net_avg_win | 63.5895 |
| net_avg_loss | -81.1298 |
| avg_hold_time_bars | 7.1710 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
