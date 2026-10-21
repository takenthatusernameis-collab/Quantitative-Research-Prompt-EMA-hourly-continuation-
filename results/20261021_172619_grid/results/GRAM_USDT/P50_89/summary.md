# EMA Hourly Continuation — GRAM/USDT P50_89

**Symbol:** GRAM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7004 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -1.9175 |
| sortino_ratio | -0.4816 |
| max_drawdown | 0.4672 |
| cagr | -0.1970 |
| net_avg_win | 64.7261 |
| net_avg_loss | -93.0177 |
| avg_hold_time_bars | 7.3180 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
