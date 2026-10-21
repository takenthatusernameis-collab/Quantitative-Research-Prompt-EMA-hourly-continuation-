# EMA Hourly Continuation — AR/USDT P34_89

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.8866 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.0965 |
| sortino_ratio | -0.6370 |
| max_drawdown | 0.5288 |
| cagr | -0.2544 |
| net_avg_win | 59.5683 |
| net_avg_loss | -76.5510 |
| avg_hold_time_bars | 10.7511 |
| exposure | 0.2219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
