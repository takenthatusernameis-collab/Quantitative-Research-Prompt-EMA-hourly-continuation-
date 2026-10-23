# EMA Hourly Continuation — ASTR/USDT P12_55

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.6399 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 1.0824 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -4.7865 |
| sortino_ratio | -2.0225 |
| max_drawdown | 0.9169 |
| cagr | -0.6221 |
| net_avg_win | 36.5863 |
| net_avg_loss | -55.0665 |
| avg_hold_time_bars | 10.2464 |
| exposure | 0.4196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
