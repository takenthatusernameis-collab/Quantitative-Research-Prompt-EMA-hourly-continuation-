# EMA Hourly Continuation — WEMIX/USDT P8_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.5025 |
| net_win_rate | 0.3816 |
| gross_profit_factor | 0.6253 |
| gross_win_rate | 0.3816 |
| sharpe_ratio | -5.3172 |
| sortino_ratio | -1.7817 |
| max_drawdown | 0.8774 |
| cagr | -0.5632 |
| net_avg_win | 40.9212 |
| net_avg_loss | -50.2571 |
| avg_hold_time_bars | 21.4187 |
| exposure | 0.5510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
