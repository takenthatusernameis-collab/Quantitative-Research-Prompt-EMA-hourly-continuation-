# EMA Hourly Continuation — TRB/USDT P12_200

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7485 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -1.3705 |
| sortino_ratio | -0.3110 |
| max_drawdown | 0.3323 |
| cagr | -0.1337 |
| net_avg_win | 74.7476 |
| net_avg_loss | -89.5018 |
| avg_hold_time_bars | 67.1680 |
| exposure | 0.7781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
