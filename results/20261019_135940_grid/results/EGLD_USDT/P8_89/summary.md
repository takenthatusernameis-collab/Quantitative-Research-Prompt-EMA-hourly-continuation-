# EMA Hourly Continuation — EGLD/USDT P8_89

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.7085 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.1196 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -3.1621 |
| sortino_ratio | -1.1747 |
| max_drawdown | 0.7748 |
| cagr | -0.4340 |
| net_avg_win | 51.6427 |
| net_avg_loss | -75.4154 |
| avg_hold_time_bars | 19.7472 |
| exposure | 0.6319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
