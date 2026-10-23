# EMA Hourly Continuation — MANTA/USDT P89_144

**Symbol:** MANTA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8385 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -4.4300 |
| sortino_ratio | -1.4132 |
| max_drawdown | 0.8242 |
| cagr | -0.4910 |
| net_avg_win | 37.6883 |
| net_avg_loss | -60.6081 |
| avg_hold_time_bars | 5.1135 |
| exposure | 0.1188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
