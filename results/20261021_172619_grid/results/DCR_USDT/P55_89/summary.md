# EMA Hourly Continuation — DCR/USDT P55_89

**Symbol:** DCR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.5772 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8516 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -3.0675 |
| sortino_ratio | -0.8365 |
| max_drawdown | 0.6224 |
| cagr | -0.3186 |
| net_avg_win | 49.7894 |
| net_avg_loss | -75.2064 |
| avg_hold_time_bars | 7.4027 |
| exposure | 0.1223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
