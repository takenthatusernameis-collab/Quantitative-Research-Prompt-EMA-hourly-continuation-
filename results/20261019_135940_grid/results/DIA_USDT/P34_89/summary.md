# EMA Hourly Continuation — DIA/USDT P34_89

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -4.7014 |
| sortino_ratio | -1.7439 |
| max_drawdown | 0.8847 |
| cagr | -0.5656 |
| net_avg_win | 41.4466 |
| net_avg_loss | -60.3577 |
| avg_hold_time_bars | 7.6212 |
| exposure | 0.2404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
