# EMA Hourly Continuation — WLD/USDT P100_200

**Symbol:** WLD/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.9642 |
| net_win_rate | 0.5374 |
| gross_profit_factor | 1.1513 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -0.1296 |
| sortino_ratio | -0.0274 |
| max_drawdown | 0.1318 |
| cagr | -0.0162 |
| net_avg_win | 93.9407 |
| net_avg_loss | -113.1761 |
| avg_hold_time_bars | 16.3037 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
