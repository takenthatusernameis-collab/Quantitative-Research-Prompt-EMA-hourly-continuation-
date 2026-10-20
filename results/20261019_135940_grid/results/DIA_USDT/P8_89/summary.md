# EMA Hourly Continuation — DIA/USDT P8_89

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.6153 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -3.9260 |
| sortino_ratio | -1.4772 |
| max_drawdown | 0.8339 |
| cagr | -0.5052 |
| net_avg_win | 39.4110 |
| net_avg_loss | -56.3615 |
| avg_hold_time_bars | 18.9292 |
| exposure | 0.6167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
