# EMA Hourly Continuation — ALT/USDT P26_200

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7340 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9395 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.9025 |
| sortino_ratio | -0.5231 |
| max_drawdown | 0.4866 |
| cagr | -0.2157 |
| net_avg_win | 70.4039 |
| net_avg_loss | -88.0533 |
| avg_hold_time_bars | 35.1631 |
| exposure | 0.5978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
