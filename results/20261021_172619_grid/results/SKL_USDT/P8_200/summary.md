# EMA Hourly Continuation — SKL/USDT P8_200

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8403 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9813 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9478 |
| sortino_ratio | -0.2467 |
| max_drawdown | 0.3686 |
| cagr | -0.1093 |
| net_avg_win | 79.9280 |
| net_avg_loss | -95.1175 |
| avg_hold_time_bars | 51.6355 |
| exposure | 0.7792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
