# EMA Hourly Continuation — DOGE/USDT P34_89

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8050 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -6.4174 |
| sortino_ratio | -2.3404 |
| max_drawdown | 0.9468 |
| cagr | -0.6889 |
| net_avg_win | 24.4681 |
| net_avg_loss | -45.4352 |
| avg_hold_time_bars | 7.5498 |
| exposure | 0.2310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
