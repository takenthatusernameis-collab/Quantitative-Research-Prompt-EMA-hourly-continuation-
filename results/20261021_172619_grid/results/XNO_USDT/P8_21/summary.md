# EMA Hourly Continuation — XNO/USDT P8_21

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.6092 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -4.3475 |
| sortino_ratio | -1.5090 |
| max_drawdown | 0.8255 |
| cagr | -0.5008 |
| net_avg_win | 49.3020 |
| net_avg_loss | -63.6183 |
| avg_hold_time_bars | 5.2091 |
| exposure | 0.1404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
