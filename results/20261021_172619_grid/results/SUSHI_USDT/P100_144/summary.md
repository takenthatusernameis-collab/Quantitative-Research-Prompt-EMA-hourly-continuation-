# EMA Hourly Continuation — SUSHI/USDT P100_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.7204 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.4664 |
| sortino_ratio | -0.3160 |
| max_drawdown | 0.3053 |
| cagr | -0.1345 |
| net_avg_win | 69.0128 |
| net_avg_loss | -97.5055 |
| avg_hold_time_bars | 6.2257 |
| exposure | 0.0637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
