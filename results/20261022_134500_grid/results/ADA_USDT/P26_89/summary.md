# EMA Hourly Continuation — ADA/USDT P26_89

**Symbol:** ADA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.4921 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8528 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -5.2020 |
| sortino_ratio | -1.9221 |
| max_drawdown | 0.9071 |
| cagr | -0.6061 |
| net_avg_win | 27.5273 |
| net_avg_loss | -47.5664 |
| avg_hold_time_bars | 9.4133 |
| exposure | 0.2961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
