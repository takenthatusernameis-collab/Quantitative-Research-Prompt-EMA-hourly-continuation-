# EMA Hourly Continuation — CERE/USDT P12_21

**Symbol:** CERE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1439 |
| net_profit_factor | 0.2072 |
| net_win_rate | 0.2335 |
| gross_profit_factor | 0.6294 |
| gross_win_rate | 0.3204 |
| sharpe_ratio | -20.5834 |
| sortino_ratio | -11.7175 |
| max_drawdown | 1.0000 |
| cagr | -0.9985 |
| net_avg_win | 7.7793 |
| net_avg_loss | -11.4359 |
| avg_hold_time_bars | 3.2147 |
| exposure | 0.2103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
