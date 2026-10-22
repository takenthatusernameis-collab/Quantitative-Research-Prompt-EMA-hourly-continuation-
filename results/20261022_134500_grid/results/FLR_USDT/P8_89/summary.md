# EMA Hourly Continuation — FLR/USDT P8_89

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.4994 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8720 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -6.9243 |
| sortino_ratio | -2.9682 |
| max_drawdown | 0.9785 |
| cagr | -0.7798 |
| net_avg_win | 22.6790 |
| net_avg_loss | -36.8459 |
| avg_hold_time_bars | 13.2740 |
| exposure | 0.5792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
