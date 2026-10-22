# EMA Hourly Continuation — ENA/USDT P34_89

**Symbol:** ENA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6566 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -3.3112 |
| sortino_ratio | -1.1948 |
| max_drawdown | 0.7625 |
| cagr | -0.4338 |
| net_avg_win | 46.1464 |
| net_avg_loss | -64.7352 |
| avg_hold_time_bars | 7.4597 |
| exposure | 0.2228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
