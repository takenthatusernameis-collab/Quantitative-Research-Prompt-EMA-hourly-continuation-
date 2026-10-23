# EMA Hourly Continuation — ZRX/USDT P8_144

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7381 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0530 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -2.0713 |
| sortino_ratio | -0.6300 |
| max_drawdown | 0.5456 |
| cagr | -0.2557 |
| net_avg_win | 63.6131 |
| net_avg_loss | -88.4709 |
| avg_hold_time_bars | 36.6310 |
| exposure | 0.7626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
