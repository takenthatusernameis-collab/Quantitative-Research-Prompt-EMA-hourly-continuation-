# EMA Hourly Continuation — PUFFER/USDT P8_26

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.7466 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.4454 |
| sortino_ratio | -0.9099 |
| max_drawdown | 0.6160 |
| cagr | -0.3429 |
| net_avg_win | 63.2819 |
| net_avg_loss | -80.8122 |
| avg_hold_time_bars | 7.8826 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
