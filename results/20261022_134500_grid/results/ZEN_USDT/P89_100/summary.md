# EMA Hourly Continuation — ZEN/USDT P89_100

**Symbol:** ZEN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.2871 |
| net_win_rate | 0.3808 |
| gross_profit_factor | 0.8116 |
| gross_win_rate | 0.4303 |
| sharpe_ratio | -9.1874 |
| sortino_ratio | -3.3711 |
| max_drawdown | 0.9869 |
| cagr | -0.8220 |
| net_avg_win | 16.1555 |
| net_avg_loss | -34.6078 |
| avg_hold_time_bars | 2.3080 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
