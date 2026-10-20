# EMA Hourly Continuation — FLUX/USDT P55_100

**Symbol:** FLUX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.4862 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8965 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -5.0752 |
| sortino_ratio | -1.8229 |
| max_drawdown | 0.9021 |
| cagr | -0.5964 |
| net_avg_win | 26.8749 |
| net_avg_loss | -50.6332 |
| avg_hold_time_bars | 5.2769 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
