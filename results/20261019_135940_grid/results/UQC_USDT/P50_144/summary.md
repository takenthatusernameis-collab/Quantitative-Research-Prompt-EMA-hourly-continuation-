# EMA Hourly Continuation — UQC/USDT P50_144

**Symbol:** UQC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.2225 |
| net_win_rate | 0.2738 |
| gross_profit_factor | 0.3757 |
| gross_win_rate | 0.2778 |
| sharpe_ratio | -6.3428 |
| sortino_ratio | -1.4175 |
| max_drawdown | 0.8360 |
| cagr | -0.5116 |
| net_avg_win | 34.6677 |
| net_avg_loss | -58.7521 |
| avg_hold_time_bars | 48.0040 |
| exposure | 0.5475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
