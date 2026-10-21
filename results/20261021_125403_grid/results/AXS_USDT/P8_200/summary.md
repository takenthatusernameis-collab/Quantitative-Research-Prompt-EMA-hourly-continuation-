# EMA Hourly Continuation — AXS/USDT P8_200

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.9537 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1232 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.2000 |
| sortino_ratio | -0.0474 |
| max_drawdown | 0.2079 |
| cagr | -0.0257 |
| net_avg_win | 90.4374 |
| net_avg_loss | -108.2652 |
| avg_hold_time_bars | 64.8235 |
| exposure | 0.7979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
