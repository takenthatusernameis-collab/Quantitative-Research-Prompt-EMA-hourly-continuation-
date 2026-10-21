# EMA Hourly Continuation — TIA/USDT P8_12

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.8709 |
| net_win_rate | 0.5343 |
| gross_profit_factor | 1.1330 |
| gross_win_rate | 0.5343 |
| sharpe_ratio | -0.5688 |
| sortino_ratio | -0.1174 |
| max_drawdown | 0.1931 |
| cagr | -0.0541 |
| net_avg_win | 80.6873 |
| net_avg_loss | -106.3041 |
| avg_hold_time_bars | 4.7206 |
| exposure | 0.0438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
