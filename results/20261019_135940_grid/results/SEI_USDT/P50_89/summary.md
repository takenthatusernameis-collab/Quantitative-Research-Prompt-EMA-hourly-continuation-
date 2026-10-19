# EMA Hourly Continuation — SEI/USDT P50_89

**Symbol:** SEI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -6.0162 |
| sortino_ratio | -2.1445 |
| max_drawdown | 0.9290 |
| cagr | -0.6488 |
| net_avg_win | 37.7030 |
| net_avg_loss | -54.4205 |
| avg_hold_time_bars | 4.8805 |
| exposure | 0.1411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
