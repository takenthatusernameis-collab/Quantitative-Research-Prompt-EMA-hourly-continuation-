# EMA Hourly Continuation — CRO/USDT P50_89

**Symbol:** CRO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.3656 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.8590 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -8.1242 |
| sortino_ratio | -3.0317 |
| max_drawdown | 0.9819 |
| cagr | -0.7943 |
| net_avg_win | 19.0374 |
| net_avg_loss | -38.5674 |
| avg_hold_time_bars | 4.6834 |
| exposure | 0.1486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
