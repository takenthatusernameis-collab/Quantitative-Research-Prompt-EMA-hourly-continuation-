# EMA Hourly Continuation — CHR/USDT P12_55

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.7203 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9048 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -2.7744 |
| sortino_ratio | -1.0224 |
| max_drawdown | 0.7085 |
| cagr | -0.3748 |
| net_avg_win | 56.2193 |
| net_avg_loss | -70.1112 |
| avg_hold_time_bars | 11.6414 |
| exposure | 0.3540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
