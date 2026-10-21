# EMA Hourly Continuation — NYM/USDT P34_144

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.4536 |
| net_win_rate | 0.3924 |
| gross_profit_factor | 0.6402 |
| gross_win_rate | 0.3924 |
| sharpe_ratio | -4.0258 |
| sortino_ratio | -0.9660 |
| max_drawdown | 0.6791 |
| cagr | -0.3637 |
| net_avg_win | 49.8696 |
| net_avg_loss | -70.9858 |
| avg_hold_time_bars | 26.5868 |
| exposure | 0.3480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
