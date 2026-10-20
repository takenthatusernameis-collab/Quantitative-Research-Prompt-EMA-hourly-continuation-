# EMA Hourly Continuation — GMT/USDT P8_20

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1741 |
| net_profit_factor | 0.2656 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.7042 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -13.2041 |
| sortino_ratio | -7.7962 |
| max_drawdown | 1.0000 |
| cagr | -0.9815 |
| net_avg_win | 4.9348 |
| net_avg_loss | -13.5087 |
| avg_hold_time_bars | 2.7478 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
