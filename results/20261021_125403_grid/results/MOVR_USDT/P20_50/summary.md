# EMA Hourly Continuation — MOVR/USDT P20_50

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.7345 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.4561 |
| sortino_ratio | -0.8321 |
| max_drawdown | 0.6713 |
| cagr | -0.3172 |
| net_avg_win | 62.4660 |
| net_avg_loss | -80.6158 |
| avg_hold_time_bars | 7.5027 |
| exposure | 0.1913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
