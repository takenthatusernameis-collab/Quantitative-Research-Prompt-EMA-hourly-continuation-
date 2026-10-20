# EMA Hourly Continuation — UQC/USDT P12_100

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.3323 |
| net_win_rate | 0.3053 |
| gross_profit_factor | 0.5367 |
| gross_win_rate | 0.3244 |
| sharpe_ratio | -6.1594 |
| sortino_ratio | -1.3842 |
| max_drawdown | 0.8479 |
| cagr | -0.5260 |
| net_avg_win | 52.7375 |
| net_avg_loss | -69.7671 |
| avg_hold_time_bars | 58.6145 |
| exposure | 0.6950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
