# EMA Hourly Continuation — GRT/USDT P8_21

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1631 |
| net_profit_factor | 0.4309 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -12.1392 |
| sortino_ratio | -6.8914 |
| max_drawdown | 0.9999 |
| cagr | -0.9708 |
| net_avg_win | 10.8943 |
| net_avg_loss | -18.7716 |
| avg_hold_time_bars | 2.9326 |
| exposure | 0.2164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
