# EMA Hourly Continuation — BSV/USDT P50_200

**Symbol:** BSV/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.5892 |
| net_win_rate | 0.4259 |
| gross_profit_factor | 0.7471 |
| gross_win_rate | 0.4259 |
| sharpe_ratio | -3.0095 |
| sortino_ratio | -0.7660 |
| max_drawdown | 0.5905 |
| cagr | -0.2974 |
| net_avg_win | 61.0914 |
| net_avg_loss | -76.9336 |
| avg_hold_time_bars | 27.2778 |
| exposure | 0.4017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
