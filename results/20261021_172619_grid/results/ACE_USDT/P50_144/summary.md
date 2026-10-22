# EMA Hourly Continuation — ACE/USDT P50_144

**Symbol:** ACE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7342 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -1.8825 |
| sortino_ratio | -0.4984 |
| max_drawdown | 0.4600 |
| cagr | -0.2054 |
| net_avg_win | 73.6414 |
| net_avg_loss | -90.9385 |
| avg_hold_time_bars | 17.7925 |
| exposure | 0.2794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
