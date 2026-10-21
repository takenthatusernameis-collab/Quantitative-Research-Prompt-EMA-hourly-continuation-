# EMA Hourly Continuation — TAO/USDT P8_50

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.9120 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0969 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.8791 |
| sortino_ratio | -0.3220 |
| max_drawdown | 0.5155 |
| cagr | -0.1434 |
| net_avg_win | 99.0303 |
| net_avg_loss | -117.6651 |
| avg_hold_time_bars | 14.0000 |
| exposure | 0.4124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
