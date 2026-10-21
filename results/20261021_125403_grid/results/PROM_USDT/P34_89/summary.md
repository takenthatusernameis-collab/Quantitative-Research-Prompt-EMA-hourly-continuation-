# EMA Hourly Continuation — PROM/USDT P34_89

**Symbol:** PROM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.5860 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8223 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -3.4896 |
| sortino_ratio | -1.0273 |
| max_drawdown | 0.6999 |
| cagr | -0.3799 |
| net_avg_win | 51.5151 |
| net_avg_loss | -70.6230 |
| avg_hold_time_bars | 11.8492 |
| exposure | 0.2321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
