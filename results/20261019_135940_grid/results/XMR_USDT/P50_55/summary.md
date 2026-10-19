# EMA Hourly Continuation — XMR/USDT P50_55

**Symbol:** XMR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.0931 |
| net_win_rate | 0.2565 |
| gross_profit_factor | 0.4862 |
| gross_win_rate | 0.3164 |
| sharpe_ratio | -18.5373 |
| sortino_ratio | -9.6216 |
| max_drawdown | 1.0000 |
| cagr | -0.9956 |
| net_avg_win | 3.5781 |
| net_avg_loss | -13.2535 |
| avg_hold_time_bars | 1.5139 |
| exposure | 0.0770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
