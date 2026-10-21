# EMA Hourly Continuation — TIA/USDT P8_200

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.9776 |
| net_win_rate | 0.5255 |
| gross_profit_factor | 1.0989 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -0.0717 |
| sortino_ratio | -0.0171 |
| max_drawdown | 0.2277 |
| cagr | -0.0128 |
| net_avg_win | 96.5655 |
| net_avg_loss | -109.4210 |
| avg_hold_time_bars | 64.7299 |
| exposure | 0.8062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
