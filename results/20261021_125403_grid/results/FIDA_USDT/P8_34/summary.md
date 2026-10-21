# EMA Hourly Continuation — FIDA/USDT P8_34

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 822 |
| net_profit_factor | 0.6865 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -3.3628 |
| sortino_ratio | -1.3716 |
| max_drawdown | 0.7966 |
| cagr | -0.4682 |
| net_avg_win | 44.1741 |
| net_avg_loss | -59.5204 |
| avg_hold_time_bars | 8.6934 |
| exposure | 0.3234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
