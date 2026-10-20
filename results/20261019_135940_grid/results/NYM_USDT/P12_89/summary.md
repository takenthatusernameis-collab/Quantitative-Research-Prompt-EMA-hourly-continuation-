# EMA Hourly Continuation — NYM/USDT P12_89

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.4043 |
| net_win_rate | 0.3904 |
| gross_profit_factor | 0.7153 |
| gross_win_rate | 0.4144 |
| sharpe_ratio | -7.2950 |
| sortino_ratio | -2.4622 |
| max_drawdown | 0.9596 |
| cagr | -0.7166 |
| net_avg_win | 28.5124 |
| net_avg_loss | -45.1667 |
| avg_hold_time_bars | 22.5257 |
| exposure | 0.5980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
