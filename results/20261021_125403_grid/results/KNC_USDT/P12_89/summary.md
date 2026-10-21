# EMA Hourly Continuation — KNC/USDT P12_89

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6665 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -3.2375 |
| sortino_ratio | -1.0281 |
| max_drawdown | 0.7253 |
| cagr | -0.3773 |
| net_avg_win | 60.7103 |
| net_avg_loss | -77.2565 |
| avg_hold_time_bars | 26.2084 |
| exposure | 0.5945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
