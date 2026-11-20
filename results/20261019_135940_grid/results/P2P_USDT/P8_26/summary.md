# EMA Hourly Continuation — P2P/USDT P8_26

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1482 |
| net_profit_factor | 0.3095 |
| net_win_rate | 0.3273 |
| gross_profit_factor | 0.5222 |
| gross_win_rate | 0.3300 |
| sharpe_ratio | -13.1838 |
| sortino_ratio | -7.1249 |
| max_drawdown | 0.9999 |
| cagr | -0.9708 |
| net_avg_win | 9.2401 |
| net_avg_loss | -14.5236 |
| avg_hold_time_bars | 4.4447 |
| exposure | 0.2994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
