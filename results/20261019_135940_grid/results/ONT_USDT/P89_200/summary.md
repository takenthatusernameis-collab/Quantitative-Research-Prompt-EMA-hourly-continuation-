# EMA Hourly Continuation — ONT/USDT P89_200

**Symbol:** ONT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5164 |
| net_win_rate | 0.4349 |
| gross_profit_factor | 0.7958 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.9619 |
| sortino_ratio | -1.1252 |
| max_drawdown | 0.7415 |
| cagr | -0.4128 |
| net_avg_win | 44.5738 |
| net_avg_loss | -66.4321 |
| avg_hold_time_bars | 11.6437 |
| exposure | 0.2144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
