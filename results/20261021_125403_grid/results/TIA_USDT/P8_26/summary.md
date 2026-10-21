# EMA Hourly Continuation — TIA/USDT P8_26

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.7852 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -1.8808 |
| sortino_ratio | -0.6845 |
| max_drawdown | 0.6163 |
| cagr | -0.2711 |
| net_avg_win | 62.0340 |
| net_avg_loss | -79.4939 |
| avg_hold_time_bars | 6.5776 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
