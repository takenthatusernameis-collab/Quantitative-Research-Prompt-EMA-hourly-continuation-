# EMA Hourly Continuation — INJ/USDT P55_89

**Symbol:** INJ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.4650 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.7830 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -5.9690 |
| sortino_ratio | -2.1301 |
| max_drawdown | 0.9291 |
| cagr | -0.6514 |
| net_avg_win | 28.1327 |
| net_avg_loss | -48.2362 |
| avg_hold_time_bars | 3.7434 |
| exposure | 0.1101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
