# EMA Hourly Continuation — XNO/USDT P100_200

**Symbol:** XNO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.5133 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8045 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -5.0943 |
| sortino_ratio | -1.6982 |
| max_drawdown | 0.8654 |
| cagr | -0.5501 |
| net_avg_win | 38.1870 |
| net_avg_loss | -56.9902 |
| avg_hold_time_bars | 7.3721 |
| exposure | 0.1846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
