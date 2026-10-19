# EMA Hourly Continuation — STX/USDT P34_55

**Symbol:** STX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.4578 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -7.2236 |
| sortino_ratio | -2.9505 |
| max_drawdown | 0.9761 |
| cagr | -0.7688 |
| net_avg_win | 21.2712 |
| net_avg_loss | -39.3506 |
| avg_hold_time_bars | 3.2630 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
