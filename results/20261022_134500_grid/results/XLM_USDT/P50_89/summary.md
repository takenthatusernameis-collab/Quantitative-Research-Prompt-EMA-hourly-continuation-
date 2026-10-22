# EMA Hourly Continuation — XLM/USDT P50_89

**Symbol:** XLM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.3613 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -6.4238 |
| sortino_ratio | -2.3006 |
| max_drawdown | 0.9485 |
| cagr | -0.6909 |
| net_avg_win | 17.4578 |
| net_avg_loss | -42.5080 |
| avg_hold_time_bars | 4.9466 |
| exposure | 0.1475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
