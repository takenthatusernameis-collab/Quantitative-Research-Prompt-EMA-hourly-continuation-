# EMA Hourly Continuation — GRAM/USDT P144_200

**Symbol:** GRAM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.3331 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7516 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.9671 |
| sortino_ratio | -1.7362 |
| max_drawdown | 0.8930 |
| cagr | -0.5832 |
| net_avg_win | 24.2612 |
| net_avg_loss | -56.4809 |
| avg_hold_time_bars | 4.6826 |
| exposure | 0.0892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
