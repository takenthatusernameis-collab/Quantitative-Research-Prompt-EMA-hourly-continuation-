# EMA Hourly Continuation — XDC/USDT P34_200

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7866 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.0678 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.3023 |
| sortino_ratio | -0.3514 |
| max_drawdown | 0.3474 |
| cagr | -0.1496 |
| net_avg_win | 66.9694 |
| net_avg_loss | -92.6988 |
| avg_hold_time_bars | 25.2635 |
| exposure | 0.4054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
