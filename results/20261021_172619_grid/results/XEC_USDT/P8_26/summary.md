# EMA Hourly Continuation — XEC/USDT P8_26

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 803 |
| net_profit_factor | 0.6293 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9336 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -4.2534 |
| sortino_ratio | -1.7256 |
| max_drawdown | 0.8711 |
| cagr | -0.5449 |
| net_avg_win | 37.7409 |
| net_avg_loss | -56.0737 |
| avg_hold_time_bars | 6.7136 |
| exposure | 0.2439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
