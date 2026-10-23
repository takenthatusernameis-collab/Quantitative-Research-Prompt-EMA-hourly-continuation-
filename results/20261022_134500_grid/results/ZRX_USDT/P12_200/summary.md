# EMA Hourly Continuation — ZRX/USDT P12_200

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6481 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -2.9595 |
| sortino_ratio | -0.8498 |
| max_drawdown | 0.6503 |
| cagr | -0.3295 |
| net_avg_win | 60.1340 |
| net_avg_loss | -82.5718 |
| avg_hold_time_bars | 38.0680 |
| exposure | 0.7129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
