# EMA Hourly Continuation — CHR/USDT P50_89

**Symbol:** CHR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.4929 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.7992 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -6.0691 |
| sortino_ratio | -2.3363 |
| max_drawdown | 0.9426 |
| cagr | -0.6721 |
| net_avg_win | 28.1981 |
| net_avg_loss | -44.4510 |
| avg_hold_time_bars | 4.8556 |
| exposure | 0.1628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
