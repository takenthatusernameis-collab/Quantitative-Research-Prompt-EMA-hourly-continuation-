# EMA Hourly Continuation — ZIL/USDT P34_89

**Symbol:** ZIL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -5.4620 |
| sortino_ratio | -2.0578 |
| max_drawdown | 0.9236 |
| cagr | -0.6281 |
| net_avg_win | 34.9699 |
| net_avg_loss | -54.1631 |
| avg_hold_time_bars | 7.0014 |
| exposure | 0.2256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
