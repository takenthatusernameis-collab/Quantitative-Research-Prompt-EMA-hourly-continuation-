# EMA Hourly Continuation — 1INCH/USDT P20_55

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6105 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -3.8494 |
| sortino_ratio | -1.3209 |
| max_drawdown | 0.7819 |
| cagr | -0.4541 |
| net_avg_win | 46.2065 |
| net_avg_loss | -64.0824 |
| avg_hold_time_bars | 8.1159 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
