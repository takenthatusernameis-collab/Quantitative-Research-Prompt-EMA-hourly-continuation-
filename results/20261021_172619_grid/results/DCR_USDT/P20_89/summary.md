# EMA Hourly Continuation — DCR/USDT P20_89

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.6768 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.5848 |
| sortino_ratio | -0.8767 |
| max_drawdown | 0.6606 |
| cagr | -0.3324 |
| net_avg_win | 49.0251 |
| net_avg_loss | -67.0373 |
| avg_hold_time_bars | 13.9278 |
| exposure | 0.3580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
